from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str: str) -> str:
    return ''.join(c for c in input_str if c.isalnum() or c in '.-_' and len(input_str) <= 255)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {"status": "error", "message": "Invalid host"}
    subprocess.call(["ping", sanitized_host])
    return {"status": "completed"}