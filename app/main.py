from fastapi import FastAPI
import subprocess
from shlex import quote
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in '._-')
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run([quote('ping'), quote(sanitized_host)], check=True, capture_output=True, text=True)
        return {"status": "completed", "result": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}