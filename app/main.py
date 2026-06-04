from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate host input
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError("Invalid host format")

    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {"status": "completed", "output": output}