# Escruta - Extractor

**Escruta Extractor** is a dedicated microservice for document parsing and content extraction within the Escruta platform. Built with Python, FastAPI and Microsoft's MarkItDown. Converts various file formats (PDF, DOCX, PPTX, XLSX, audio, and YouTube URLs) into clean Markdown for AI processing.

> [!IMPORTANT]
> This service is a required component of the Escruta ecosystem. It must be accessible to the Core service for proper document processing and ingestion.

## Getting Started

### Prerequisites

- Python (version 3.12 or higher).
- [uv](https://docs.astral.sh/uv/) package manager.

### Installation

1. `uv sync` - Install dependencies
2. `uv run fastapi dev` - Start the development server

The extraction service will be available at [localhost:8000](http://localhost:8000) by default.

## Configuration

### Environment Variables

The application is secured and configured using environment variables. These must be set in your `.env` file or environment.

| Variable                   | Description                                           | Default    |
| -------------------------- | ----------------------------------------------------- | ---------- |
| `ESCRUTA_INTERNAL_API_KEY` | Internal API Key for service-to-service communication | (Required) |

### Development Scripts

- `uv run fastapi dev` - Start development server with auto-reload
- `uv run fastapi run` - Start production server

## Technology Stack

- **Runtime**: Python 3.12+ with [uv](https://docs.astral.sh/uv/) for lightning-fast dependency management.
- **Framework**: FastAPI for high-performance, robust API endpoints.
- **Extraction**: Microsoft MarkItDown for reliable document-to-markdown conversion, including support for rich media, spreadsheets, and audio transcription.
