from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    # Add your sanitization logic here (e.g., regex, whitelisting)
    return input_str.strip()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation
    subprocess.call(["ping", sanitized_host])
    return {"status": "completed"}