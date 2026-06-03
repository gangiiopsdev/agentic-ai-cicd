from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host: str) -> str:
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(c for c in host if c in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    # Safe implementation using subprocess.run with shell=False and split command line
    result = subprocess.run(['ping', '-c', '1', f'--{sanitized_host}'], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}