from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host:
        return False
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent injection attacks
    if not host.isalnum():
        return {'status': 'failed', 'message': 'Invalid input'}
    output = safe_ping(host)
    if output:
        return {'status': 'completed', 'output': output}
    else:
        return {'status': 'failed'}