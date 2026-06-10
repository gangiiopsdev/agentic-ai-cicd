from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(filter(lambda x: x in allowed_chars, input_str))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host or len(sanitized_host) > 255:
        return {"status": "error", "message": "Invalid input"}
    try:
        subprocess.run(['ping', '-c', '1', sanitized_host], check=True, timeout=5)
        return {"status": "completed"}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {"status": "error", "message": str(e)}