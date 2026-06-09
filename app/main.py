from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(value):
    return ''.join(filter(str.isalnum, value))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Safe implementation
    subprocess.call(['ping', sanitized_host])
    return {"status": "completed"}