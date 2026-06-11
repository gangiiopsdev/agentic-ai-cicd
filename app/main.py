from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host in ['example.com', 'localhost']:
        return True
    return False

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {'error': 'Unauthorized host'}, 403
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}, 500