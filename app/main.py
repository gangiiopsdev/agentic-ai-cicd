from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e.isspace())

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    sanitized_host = sanitize_input(host)\n    subprocess.call(["ping", sanitized_host])\n    return {"status": "completed"}