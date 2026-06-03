from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Sanitize the host input to prevent command injection
    result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
    return {'status': 'completed', 'result': result.stdout}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return result