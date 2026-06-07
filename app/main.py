from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    # Implement input sanitization logic here
    return ''.join(c for c in input_str if c.isalnum() or c in '._-')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', sanitized_host]
    subprocess.call(args)

    return {"status": "completed"}