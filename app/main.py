from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isnumeric():
        return {'status': 'error', 'message': 'Invalid host'}
    # Sanitize input further if necessary
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'success', 'output': result.stdout}
app = FastAPI()
@app.get("/ping")
def ping(host: str):    return safe_ping(host)