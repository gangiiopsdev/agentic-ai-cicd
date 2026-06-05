from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_hosts = ['example.com', 'localhost']  # Define a whitelist of allowed hosts
    if host in allowed_hosts:
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True, shell=False)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output}
    else:
        return {'status': 'failed', 'error': 'Host not allowed'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)