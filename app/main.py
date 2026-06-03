from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host or '||' in host or ';' in host or '&' in host:
        return {'status': 'error', 'message': 'Invalid input'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result['status'] == 'error':
        return result
    return result