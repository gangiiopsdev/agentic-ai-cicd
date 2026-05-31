from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation
    try:
        output = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        return {'status': 'error', 'result': 'Invalid input'}
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}