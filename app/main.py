from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not host.strip():
        raise ValueError('Host cannot be empty')
    ping_command = ['ping', host]
    result = subprocess.run(ping_command, capture_output=True, text=True, check=False)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    output = safe_ping(host)
    return {"status": "completed", "output": output}