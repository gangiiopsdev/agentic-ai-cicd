from fastapi import FastAPI
import subprocess
def secure_ping(host: str):
    # Sanitize input to prevent command injection
    if not all(c.isalnum() or c in ' .-\/' for c in host):
        return {'error': 'Invalid host'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    result = secure_ping(host)
    if 'error' in result:
        return result
    else:
        subprocess.call(["ping", host])
        return {'status': 'completed'}