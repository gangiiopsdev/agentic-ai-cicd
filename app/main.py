from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.strip():
        return False, 'Invalid input'
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, str(e)

@app.get("/ping")
def ping(host: str):
    success, output = safe_ping(host)
    if not success:
        return {'status': 'failed', 'error': output}
    else:
        return {'status': 'completed', 'output': output}