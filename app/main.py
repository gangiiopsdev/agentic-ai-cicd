from fastapi import FastAPI
import subprocess
from shlex import quote
def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(char for char in host if char in allowed_chars)

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    sanitized_host = sanitize_host(host)\n    try:\n        result = subprocess.run(['ping', quote(sanitized_host)], capture_output=True, text=True, check=True)\n        return {"status": "completed", "output": result.stdout}\n    except subprocess.CalledProcessError as e:\n        return {"status": "failed", "error": str(e)}