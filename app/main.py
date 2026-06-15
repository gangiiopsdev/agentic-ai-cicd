from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    # Implement input sanitization logic here
    return ''.join(e for e in input_str if e.isalnum() or e in ['-', '.', '_', ' '])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.check_output(['ping', sanitized_host], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}