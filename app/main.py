from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host.strip() and all(c.isalnum() or c in '.-' for c in host):
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)