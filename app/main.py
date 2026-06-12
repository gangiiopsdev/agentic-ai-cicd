from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c in ('.', '-', '_'))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', sanitized_host]
    subprocess.call(args)
    return {"status": "completed"}