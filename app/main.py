from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation
    try:
        subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)