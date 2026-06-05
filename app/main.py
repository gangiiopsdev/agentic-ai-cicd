from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(char for char in host if char in allowed_chars)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = sanitize_host(host)
    command = ['ping', safe_host]
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return {"status": "completed", "output": result.stdout}