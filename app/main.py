from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Use a full path for the executable to avoid shell injection risks
        subprocess.run(['/usr/bin/ping', host], check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)