from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid input")
    subprocess.call(f'ping {host}')

@app.get="/ping")
def ping(host: str):
    try:
        return {'status': 'completed', 'output': safe_ping(host)}
    except Exception as e:
        return {'error': str(e)}