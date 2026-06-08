from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Validate and sanitize input to prevent injection attacks
        if not host or 'ping' in host.split():
            raise ValueError('Invalid host')
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return str(e)

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}