from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ['.', '-', '_'])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent injection
    sanitized_host = sanitize_input(host)
    subprocess.run(["ping", sanitized_host], check=True, capture_output=True, text=True)
    return {"status": "completed"}