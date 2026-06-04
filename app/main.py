from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.strip():
        raise ValueError('Host parameter cannot be empty')
    # Safe implementation using list for the command
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    try:
        response = safe_ping(host)
        return {'status': 'completed', 'output': response}
    except ValueError as e:
        return {'error': str(e)}, 400