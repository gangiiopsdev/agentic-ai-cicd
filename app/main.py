from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() and not e.isspace())

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if len(sanitized_host) > 50:
        return {"status": "error", "message": "Invalid host"}
    subprocess.call(['ping', sanitized_host])
    return {"status": "completed"}