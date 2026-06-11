from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and sanitization
    if not host.isalnum():
        return {'error': 'Invalid host'}, 400
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}