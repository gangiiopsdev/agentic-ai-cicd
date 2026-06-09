from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isdigit():
        return 'Invalid input'
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, timeout=5, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)