from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation using check_output and avoiding shell=True
    try:
        result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'result': result}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.output)}

@app.get("/ping")
def ping_host(host: str):
    return ping(host)