from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e.isspace())
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Avoid using subprocess with shell=True and ensure the command is constructed safely
    subprocess.run(["ping", sanitized_host], check=True, capture_output=True, text=True)
    return {"status": "completed"}