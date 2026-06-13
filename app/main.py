from fastapi import FastAPI
import subprocess
from urllib.parse import quote

def safe_ping(host: str) -> dict:
    # Sanitize the host input
    safe_host = quote(host)
    try:
        result = subprocess.run(['ping', safe_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)