from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str: str) -> str:
    return ''.join(c for c in input_str if c.isalnum() or c in '.-_' and len(input_str) <= 255)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {"status": "error", "message": "Invalid host"}
    subprocess.run(shlex.split(f'ping {sanitized_host}'), check=True, capture_output=True, text=True)
    return {"status": "completed"}