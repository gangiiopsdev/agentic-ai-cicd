from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(char for char in input_string if char in allowed_chars)

@app.get("/ping")
def ping(host: str):\n    sanitized_host = sanitize_input(host)\n    try:\n        result = subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)\n        return {"status": "completed", "output": result.stdout}\n    except subprocess.CalledProcessError as e:\n        return {"status": "failed", "error": e.stderr}