from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    # Implement input sanitization logic here
    return '127.0.0.1'  # Example sanitization

@app.get("/ping")
def ping(host: str):

    sanitized_host = sanitize_input(host)
    subprocess.call(f"ping {sanitized_host}")

    return {"status": "completed"}