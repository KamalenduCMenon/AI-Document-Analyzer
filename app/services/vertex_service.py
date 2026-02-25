import vertexai
from vertexai.generative_models import GenerativeModel
import os

def analyze_document(text: str):

    vertexai.init(
        project=os.getenv("GCP_PROJECT"),
        location="us-central1"
    )

    model = GenerativeModel("gemini-2.0-flash")

    prompt = f"""
    Analyze the following document and provide:

    1. Summary
    2. Key Risks
    3. Sentiment

    Document:
    {text}
    """

    response = model.generate_content(prompt)

    return response.text