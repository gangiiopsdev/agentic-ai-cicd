from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    # Add input sanitization logic here, e.g., using regex or a whitelist of allowed characters.
    return ''.join(e for e in input_string if e.isalnum() or e in '._-')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        subprocess.call(["ping", sanitized_host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}