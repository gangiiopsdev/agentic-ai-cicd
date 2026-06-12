from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    cmd = ['ping', host]
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}