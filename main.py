from fastapi import FastAPI, UploadFile, File, HTTPException, Form, Security, Depends
from fastapi.security.api_key import APIKeyHeader
from markitdown import MarkItDown
import os
import shutil
import tempfile
import requests

api_key_header = APIKeyHeader(name="ESCRUTA_INTERNAL_API_KEY", auto_error=False)


def verify_token(x_token: str = Security(api_key_header)):
    api_key = os.getenv("ESCRUTA_INTERNAL_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="Server Configuration Error")

    if not x_token or x_token != api_key:
        raise HTTPException(status_code=401, detail="Invalid or missing API Key")
    return x_token


app = FastAPI(dependencies=[Depends(verify_token)])
md = MarkItDown()


@app.post("/extract")
async def extract_content(file: UploadFile = File(None), url: str = Form(None)):
    if not file and not url:
        raise HTTPException(status_code=400, detail="Provide a file or a URL")

    try:
        if file:
            filename = file.filename or ""
            suffix = os.path.splitext(filename)[1]
            with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
                shutil.copyfileobj(file.file, tmp)
                result = md.convert(tmp.name)
            os.unlink(tmp.name)
        else:
            headers = {"User-Agent": "EscrutaExtractorBot/1.0 (+https://escruta.com)"}
            response = requests.get(url, headers=headers, timeout=15)
            response.raise_for_status()
            result = md.convert(response)

        title = getattr(result, "title", None)
        if not title and file and file.filename:
            title = os.path.splitext(file.filename)[0]

        return {"title": title, "content": result.text_content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
