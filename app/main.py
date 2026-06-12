from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(user_input):
    # Implement appropriate sanitization logic here
    return ''.join(c for c in user_input if c.isalnum() or c in ['-', '.', '_', ' ', '/'])

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {"status": "completed"}