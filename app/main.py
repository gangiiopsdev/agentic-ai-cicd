from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(c for c in input_string if c in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        subprocess.check_output(['ping', sanitized_host], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}

    return {"status": "completed"}