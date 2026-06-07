from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if 'ping' not in host:
        return {'error': 'Unsafe input detected'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)