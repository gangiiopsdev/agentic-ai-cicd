from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(filter(lambda x: x.isalnum() or x in ('.', '-'), input_str))

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": subprocess.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "stderr": str(e.stderr)}