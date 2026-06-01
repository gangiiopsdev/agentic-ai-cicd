from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input):
    if '&&' in input or ';' in input or '|' in input:
        raise ValueError('Invalid characters detected in input')
    return input

@app.get("/ping")
def ping(host: str):    sanitized_host = sanitize_input(host)
    subprocess.call(f"ping {sanitized_host}", shell=True)
    return {"status": "completed"}