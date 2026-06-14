from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(ch for ch in input_str if ch.isalnum() or ch in '._-')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(["ping", "-c", "4", sanitized_host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}