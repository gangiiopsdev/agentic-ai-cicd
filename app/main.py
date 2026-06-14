from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Using subprocess.run instead of subprocess.call for better security
        result = subprocess.run(['/usr/bin/ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)