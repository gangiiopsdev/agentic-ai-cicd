from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in input_str if char in allowed_chars)

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input
    sanitized_host = sanitize_input(host)

    try:
        subprocess.call(['ping', '-c 1', sanitized_host], timeout=5, shell=False)
        return {"status": "completed", "host": sanitized_host}
    except Exception as e:
        return {"status": "error", "message": str(e)}, 400