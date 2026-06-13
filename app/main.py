from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isdigit():
        return False
    try:
        output = subprocess.check_output(['ping', '-c', '4', host], stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.output, 'utf-8')

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if not result:
        return {'error': 'Invalid host'}
    return {'status': 'completed', 'result': result}