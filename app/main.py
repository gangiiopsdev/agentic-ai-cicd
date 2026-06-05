from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/""
)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "failed", "error": "Invalid host input"}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        # Sanitize the output to prevent information disclosure
        sanitized_output = re.sub(r'[^a-zA-Z0-9\s]', '', result.stdout)
        return {"status": "completed", "output": sanitized_output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}