from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(value):
    return ''.join(c for c in value if c.isalnum() or c in ' .,-')

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    sanitized_host = sanitize_input(host)
    subprocess.call(["ping", sanitized_host])
    return {"status": "completed"}