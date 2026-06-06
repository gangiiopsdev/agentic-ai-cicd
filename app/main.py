from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host or not host.isalnum():
        return False
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return True, result.stdout
    except Exception as e:
        return False, str(e)

@app.get("/ping")
def ping(host: str):
    success, output = safe_ping(host)
    if success:
        return {'status': 'completed', 'output': output}
    else:
        return {'status': 'error', 'message': output}