from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Simple input sanitization example
    return ''.join(filter(lambda x: x.isalnum(), input_string))

@app.get("/ping")
def ping(host: str):

    sanitized_host = sanitize_input(host)

    # Safe implementation with validation and escaping
    subprocess.run(['ping', '--', sanitized_host], check=True)

    return {"status": "completed"}