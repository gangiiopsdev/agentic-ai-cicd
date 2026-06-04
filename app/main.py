from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        # Use a list of arguments for subprocess call to avoid shell injection
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)