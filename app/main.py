from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isdigit():
        raise ValueError('Invalid host')
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f'Error: {str(e)}'

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}