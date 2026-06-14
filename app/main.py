from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate host to prevent shell injection attacks
    if not host.strip().endswith('.com'):
        raise ValueError('Invalid host format')
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        result = ping(host)
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}
    return {'status': 'completed', 'result': result}