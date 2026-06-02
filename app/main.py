from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return input_string.strip().replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):

    # Sanitize input to prevent command injection
    sanitized_host = sanitize_input(host)

    # Safe implementation
    subprocess.call(['ping', sanitized_host])

    return {"status": "completed"}