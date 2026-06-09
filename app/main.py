from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Sanitize host to avoid shell injection
        host = subprocess.quote(host)
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'output': safe_ping(host)}