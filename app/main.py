from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    # Sanitize user input
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized = ''.join(char for char in host if char in allowed_chars)
    return sanitized

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    try:
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, shell=False)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "error", "message": str(e)}