from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'stdout': None, 'stderr': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)