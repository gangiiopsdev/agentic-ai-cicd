from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    # Add your input sanitization logic here
    return ''.join(e for e in input_str if e.isalnum() or e.isdigit())

@app.get("/ping")
def ping(host: str):

    sanitized_host = sanitize_input(host)

    # Safe implementation
    subprocess.call(['ping', sanitized_host])

    return {"status": "completed"}