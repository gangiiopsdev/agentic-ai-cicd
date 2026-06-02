from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Implement input sanitization logic here
    return input_string.strip()

@app.get="/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Use safe method for executing commands without shell=True
    subprocess.call(['ping', sanitized_host])
    return {"status": "completed"}