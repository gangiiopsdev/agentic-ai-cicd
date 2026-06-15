from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(user_input):
    # Implement input sanitization logic here
    return user_input.strip()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(['ping', sanitized_host])
    return {"status": "completed"}