from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(host):
    return ''.join(e for e in host if e.isalnum() or e == '.' or e == '-')

@app.get("/ping")
def ping(host: str):
    # Sanitize input
    sanitized_host = sanitize_input(host)
    if not sanitized_host.strip():
        return {"error": "Host parameter is empty, invalid, or contains special characters"}
    args = ['ping', sanitized_host]
    subprocess.run(args, check=True)
    return {"status": "completed"}