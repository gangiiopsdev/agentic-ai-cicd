from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    if 'ping' in input_str or 'shell' in input_str:
        raise ValueError('Input contains disallowed keywords')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
    return {"status": "completed"}