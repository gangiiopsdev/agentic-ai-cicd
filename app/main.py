from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    return ['ping', host]

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(safe_ping(host), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}