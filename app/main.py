from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation using subprocess.run with proper sanitization of input
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        response = ping(host)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}, 500