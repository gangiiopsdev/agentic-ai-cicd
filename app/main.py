from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    # Implement input sanitization logic here
    return ''.join(e for e in input_string if e.isalnum() or e.isspace())

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(shlex.split(f"ping {sanitized_host}"))
    return {"status": "completed"}