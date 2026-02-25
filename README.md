# AI Document Analyzer

A cloud-deployed AI-powered document analyzer using **Google Vertex AI Gemini 2.0**.  
Provides a REST API to extract summaries, key points, and insights from textual documents. Built with **FastAPI** and deployed on **Google Cloud Run**.

---
## Features

- Text analysis using **Gemini 2.0**  
- REST API endpoints with **FastAPI**  
- Serverless deployment on **Cloud Run** (auto-scaling)  
- Secure authentication via **Application Default Credentials (ADC)**  

---
## Architecture

            +----------------------+
            |     Client / UI      |
            | (Browser / Postman)  |
            +----------+-----------+
                       |
                       v
            +----------------------+
            |   Cloud Run Service  |
            |  (FastAPI Application)|
            +----------+-----------+
                       |
                       v
            +----------------------+
            | Vertex AI Gemini 2.0 |
            |   (Text Analysis)    |
            +----------+-----------+
                       |
                       v
            +----------------------+
            |       Response       |
            |   JSON with summary, |
            |   key points, insights|
            +----------------------+

### How It Works

1. **Client sends request** → `/analyze?text=<document text>`  
2. **FastAPI service** on Cloud Run receives request  
3. Calls **Vertex AI Gemini 2.0** for analysis  
4. Gemini returns **summary, key points, insights**  
5. FastAPI responds with structured JSON to client

---
## Tech Stack

- **Backend**: Python, FastAPI  
- **AI Service**: Google Vertex AI Gemini 2.0  
- **Deployment**: Cloud Run, Cloud Build  
- **Containerization**: Docker  
- **CI/CD**: GitHub integration  

---
## Setup & Deployment

### Local

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```
Access Swagger UI: http://127.0.0.1:8000/docs

### Cloud Run
- Push code to GitHub.
- Cloud Console → Cloud Run → Create Service → Deployment source: GitHub
- Select branch & directory with Dockerfile
- Configure service (name, region us-central1, scaling, memory)
- Access API via the provided Cloud Run URL

---
## Folder Structure
```
ai-document-analyzer/
├── main.py
├── app/services/vertex_service.py
├── requirements.txt
├── Dockerfile
├── .env (optional)

```
