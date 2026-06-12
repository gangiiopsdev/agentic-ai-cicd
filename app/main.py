from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Sanitize the input to avoid command injection
        host = subprocess.quote(host)
        response = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return response.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)