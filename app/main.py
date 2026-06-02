from fastapi import FastAPI
import subprocess
from urllib.parse import quote

app = FastAPI()

def ping(host: str):
    # Sanitize the host input before using it in the subprocess call
    safe_host = ''.join(c for c in host if c.isalnum() or c.isdigit() or c == '.' or c == '-' or c == '_')
    args = ['ping', '--count=1', quote(safe_host)]
    subprocess.run(args, check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_host = ''.join(c for c in host if c.isalnum() or c.isdigit() or c == '.' or c == '-' or c == '_')
    args = ['ping', '--count=1', quote(safe_host)]
    subprocess.run(args, check=True)
    return {"status": "completed"}