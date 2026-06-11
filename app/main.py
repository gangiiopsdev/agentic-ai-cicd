from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Ping failed: {e.output}"

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    return safe_ping(host)