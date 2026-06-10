from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True)

def sanitize_input(input_string: str) -> str:
    # Implement input sanitization logic here
    return ''.join(c for c in input_string if c.isalnum())

@app.get("/ping")
def ping_endpoint(host: str):
    sanitized_host = sanitize_input(host)
    ping(sanitized_host)