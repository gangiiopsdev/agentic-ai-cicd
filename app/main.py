from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    if not input_string.isalnum():
        raise ValueError("Invalid input")

app = FastAPI()

@app.get="/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', sanitized_host]
    subprocess.call(args)
    return {"status": "completed"}