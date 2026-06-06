from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)