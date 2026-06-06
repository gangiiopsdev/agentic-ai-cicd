from fastapi import FastAPI
import subprocess
global ping_result = {}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        ping_result[host] = output.decode('utf-8')
        return {'status': 'completed', 'result': output.decode('utf-8')}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'failed', 'error': str(e)}