from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    # Implement input sanitization logic here
    return input_string.strip()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}