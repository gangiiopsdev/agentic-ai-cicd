from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    # Implement proper input sanitization logic here
    return ''.join(e for e in input_str if e.isalnum())

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.run(shlex.split(f"ping {sanitized_host}"), check=True, shell=False)
    return {"status": "completed"}