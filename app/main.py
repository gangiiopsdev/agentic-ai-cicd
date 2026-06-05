from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(user_input):
    # Implement proper input sanitization here
    return user_input.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(f"ping {sanitized_host}", shell=True)
    return {"status": "completed"}