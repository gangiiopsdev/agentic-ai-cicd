from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    # Simple sanitization, in production use a proper library or function
    return ''.join(e for e in input_str if e.isalnum() and 'a' <= e <= 'z')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(f"ping {sanitized_host}", shell=False)

    return {"status": "completed"}