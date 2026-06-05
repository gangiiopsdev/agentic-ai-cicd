from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() and e.isprintable())

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if len(sanitized_host) > 50:
        raise ValueError("Invalid host")
    subprocess.call(["ping", sanitized_host], shell=False)
    return {"status": "completed"}