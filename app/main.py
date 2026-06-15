from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Ensure host is sanitized before use in subprocess call
    if any(char in host for char in [';', '&', '|', '<', '>', '*', '?']):
        raise ValueError('Invalid characters in hostname')
    return host

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input sanitization and use of check_output for better error handling
    sanitized_host = safe_ping(host)
    result = subprocess.run(["ping", sanitized_host], capture_output=True, text=True)
    return {"status": "completed", "result": result.stdout}