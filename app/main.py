from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    # Safe implementation with input validation
    if not all(c.isalnum() or c in '.-@' for c in host):
        raise ValueError("Invalid host name")
    output = safe_ping(host)
    return {"status": "completed", "output": output}