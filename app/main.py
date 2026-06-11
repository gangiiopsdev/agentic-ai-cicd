from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c == '.' or c == ':')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    # Validate and sanitize host input
    if not host:
        raise ValueError("Invalid host input")
    subprocess.call(['ping', host])
    return {"status": "completed"}