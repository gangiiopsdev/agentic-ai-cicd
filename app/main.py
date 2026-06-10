from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

def sanitize_input(input_str):
    # Add your sanitization logic here, e.g., using regex or a whitelist
    return ''.join(e for e in input_str if e.isalnum() and not e.isspace())

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.run(["ping", sanitized_host], capture_output=True, text=True, check=True)
        return JSONResponse(content={"status": "completed", "output": output.stdout}, status_code=200)
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={"status": "failed", "error": str(e)}, status_code=500)