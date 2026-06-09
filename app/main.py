from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate host input to prevent command injection
    if not all(c.isalnum() or c in ['-', '.'] for c in host):
        raise ValueError('Invalid host name')
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {"status": "completed", "output": output}