from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        if result.returncode == 0:
            return {'status': 'completed'}
        else:
            return {'status': 'failed', 'message': result.stderr}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)