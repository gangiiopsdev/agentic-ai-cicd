from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)