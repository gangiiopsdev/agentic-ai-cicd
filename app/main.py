from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in host if char in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    try:
        result = subprocess.run(['ping', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {"status": "completed", "stdout": result.stdout, "stderr": result.stderr}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "stdout": str(e.output), "stderr": str(e.stderr)}