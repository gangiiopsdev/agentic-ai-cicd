from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    if host in ['127.0.0.1', '::1']:  # Whitelist specific hosts
        return safe_ping(host)
    else:
        return {'status': 'failed', 'error': 'Host not allowed'}