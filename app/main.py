from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate host input to prevent shell injection
    if not all(c.isalnum() or c in '.-' for c in host):
        raise ValueError("Invalid hostname")

@app.get="/ping")
def ping(host: str):
    try:
        result = subprocess.run(['ping', safe_ping(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}