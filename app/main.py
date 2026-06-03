from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Safe implementation with output capturing and handling
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        response = safe_ping(host)
        return {'status': 'completed', 'output': response}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}