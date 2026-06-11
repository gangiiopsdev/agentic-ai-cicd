from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    if not input_string.isalnum():
        raise ValueError("Invalid input")
    return input_string

@app.get="/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(f"ping {sanitized_host}", shell=False)
    return {"status": "completed"}