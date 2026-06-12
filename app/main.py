from fastapi import FastAPI
import subprocess
global host

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host:
        return {'status': 'failed', 'error': 'Host is required'}
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}