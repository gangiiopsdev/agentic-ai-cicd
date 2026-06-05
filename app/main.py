from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(value: str) -> str:
    return ''.join(e for e in value if e.isalnum() or e in ('.', '-', '_'))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', sanitized_host]
    subprocess.call(args)
    return {"status": "completed"}