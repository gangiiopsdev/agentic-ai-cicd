from fastapi import FastAPI
import subprocess
def validate_host(host):
    return all(c.isalnum() or c in ['-', '.', '_'] for c in host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'message': 'Invalid host name'}
    try:
        result = subprocess.check_output(['ping', f'-c 1 {host}'], stderr=subprocess.STDOUT, shell=True)
        return {'status': 'completed', 'message': 'Ping successful', 'result': result.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'message': str(e.output)}