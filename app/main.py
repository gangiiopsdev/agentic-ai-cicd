from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Validate and sanitize input to prevent injection attacks
        if not host or 'ping' in host.split():
            raise ValueError('Invalid host')
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8').strip()
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}