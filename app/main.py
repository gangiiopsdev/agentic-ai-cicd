from fastapi import FastAPI
import subprocess
def sanitize_input(user_input):
    # Add your input sanitization logic here
    return user_input.strip()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(["ping", sanitized_host])
    return {"status": "completed"}