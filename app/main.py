from fastapi import FastAPI
from app.schemas import EmailRequest, EmailResponse
from app.ai_service import analyze_email
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Email Analyzer API")


app.add_middleware(
    CORSMiddleware,
 allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze-email", response_model=EmailResponse)
async def analyze(request: EmailRequest):
    category, response = analyze_email(request.content)

    return EmailResponse(
        category=category,
        suggested_response=response
    )
