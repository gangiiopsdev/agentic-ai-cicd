from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum())

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    host = sanitize_input(host)
    if not host:
        raise ValueError("Invalid host name")
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}