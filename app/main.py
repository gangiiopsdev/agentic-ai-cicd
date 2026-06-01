from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.output.decode()}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    return execute_ping(host)