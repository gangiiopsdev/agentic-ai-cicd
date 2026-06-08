from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    # Add your sanitization logic here
    return input_str.strip()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(['ping', sanitized_host])
    return {"status": "completed"}