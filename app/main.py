from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Safe implementation using subprocess.run
        result = subprocess.run(['ping', host], check=True)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)