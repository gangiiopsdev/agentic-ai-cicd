from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(value: str) -> str:
    return ''.join(c for c in value if c.isalnum() or c in ('-', '.'))

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    sanitized_host = sanitize_input(host)
    subprocess.run(['ping', sanitized_host], check=True)
    return {"status": "completed"}