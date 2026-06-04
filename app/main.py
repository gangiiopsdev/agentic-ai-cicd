from fastapi import FastAPI
import subprocess

def safe_ping(host):
    if host.isalnum() and len(host) <= 64:
        # Sanitize the host by escaping special characters that could be used for command injection
        sanitized_host = ''.join(char if char.isalnum() else '_' for char in host)
        return subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    else:
        return None

app = FastAPI()

@app.get("/ping")
def ping(host: str): 
    result = safe_ping(host)
    if result is not None:
        return result.stdout
    else:
        return "Invalid host"