from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return ' '.join(filter(lambda x: str(x).strip().isalnum() or str(x).strip() in ['-', '_', '.'], input_string.split()))

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        subprocess.run(['ping', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    return {"status": "completed"}