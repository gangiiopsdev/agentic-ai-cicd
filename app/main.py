from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return run_ping(host)