from fastapi import FastAPI
import subprocess
def ping(host: str):
    if not host:
        return {'status': 'failed', 'error': 'Host is required'}
    try:
        output = subprocess.run(['ping', '-c', '1', f'/bin/ping {host}'], capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)