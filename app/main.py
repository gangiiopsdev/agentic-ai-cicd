from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    host = host.strip()  # Sanitize input by stripping leading/trailing whitespace
    if not all(c.isalnum() or c in ['.', '-'] for c in host):  # Check for allowed characters
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {"status": "completed", "output": response}