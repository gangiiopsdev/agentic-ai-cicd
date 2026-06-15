from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safer implementation using subprocess with validation
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    try:
        result = subprocess.run(['ping', '-c', '4', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {"status": "completed", "output": output}