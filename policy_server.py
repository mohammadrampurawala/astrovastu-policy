from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Privacy Policy Server Active", "docs": "/privacy-policy"}

@app.get("/privacy-policy", response_class=PlainTextResponse)
def privacy_policy():
    return """
    AstroVastu GPT - Privacy Policy
    --------------------------------
    Last Updated: October 2025

    We respect your privacy and only use provided data (like name, date, time, and place of birth)
    to generate astrological insights. No personal data is stored or shared.
    Do not enter financial or sensitive information.

    Contact: support@astrovastu.ai
    """
