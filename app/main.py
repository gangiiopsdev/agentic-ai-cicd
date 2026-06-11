from fastapi import FastAPI
import subprocess
from shlex import quote
def sanitize_input(input_str):
    return ' '.join(quote(part) for part in input_str.split())
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.run(['ping', '-c 1', sanitized_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}