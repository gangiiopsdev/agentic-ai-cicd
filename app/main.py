from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.output, 'utf-8')

@app.get("/ping")
def ping(host: str):
    if not host or len(host) > 255 or any(char in host for char in [';', '|', '&', '<', '>']):
        return {'status': 'error', 'result': 'Invalid input'}
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}