from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input):
    return ''.join(e for e in input if e.isalnum() or e in ['.', '-', '_'])

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation
    subprocess.call(['ping', sanitized_host])

    return {"status": "completed"}