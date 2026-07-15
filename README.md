# Escruta - Extractor

> [!CAUTION]
> **This repository has been deprecated.**
> Its functionality has been merged into the unified [Helper](https://github.com/escruta/helper) service.

Dedicated microservice for document parsing and content extraction within the Escruta platform. Converts various file formats (PDF, DOCX, PPTX, XLSX, audio, and YouTube URLs) into clean Markdown for AI processing.

Built with Python, FastAPI, and MarkItDown.

> [!IMPORTANT]
> This service is a required component of the Escruta ecosystem. It must be accessible to the Core service for proper document processing and ingestion.

## Getting Started

1. `uv sync` - Install dependencies
2. `uv run --env-file .env fastapi run --port 8000` - Start the development server

The extraction service will be available at [localhost:8000](http://localhost:8000). It is consumed by [Core](https://github.com/escruta/core) at this URL (configured via `ESCRUTA_EXTRACTOR_URL`).

## Configuration

### Environment Variables

The application is secured and configured using environment variables. These must be set in your `.env` file or environment.

| Variable                   | Description                                           | Default    |
| -------------------------- | ----------------------------------------------------- | ---------- |
| `ESCRUTA_INTERNAL_API_KEY` | Internal API Key for service-to-service communication | (Required) |
