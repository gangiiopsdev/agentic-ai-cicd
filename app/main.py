from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate the host input to prevent injection attacks
    if not host.isdigit():
        raise ValueError("Invalid host")
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        response = safe_ping(host)
        return {'status': 'completed', 'response': response}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}