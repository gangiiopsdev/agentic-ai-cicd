from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the URL to prevent directory traversal attacks
        parsed_url = urlparse(host)
        if not all([parsed_url.scheme, parsed_url.netloc]):
            raise ValueError("Invalid host URL")
        # Using parameterized command to prevent shell injection
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    except ValueError as ve:
        return {"status": "failed", "error": str(ve)}