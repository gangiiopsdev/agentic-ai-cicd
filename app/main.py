from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ['-', '.', '_', ' ', '!', '+', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '{', '}', '[', ']', '|', '\', ':', ';', '<', ',', '>', '?', '/', '~'])

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {"status": "invalid input"}

    # Safer implementation using subprocess.run instead of subprocess.call to avoid shell=True and command injection
    subprocess.run(['ping', '-c', '1', sanitized_host], check=True, capture_output=True, text=True)

    return {"status": "completed"}