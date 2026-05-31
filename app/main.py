from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent shell injection
    if not all(c.isalnum() or c in ('-', '.', '_', '@', ':') for c in host):
        raise ValueError("Invalid characters in host")
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}