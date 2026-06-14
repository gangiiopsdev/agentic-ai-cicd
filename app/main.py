from fastapi import FastAPI
import subprocess
def sanitize_input(input):
    return ''.join(e for e in input if e.isalnum() or e.isspace())
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation
    subprocess.call(['ping', '-c', '1', sanitized_host], shell=False)
    return {"status": "completed"}