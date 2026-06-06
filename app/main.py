from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host):
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host in allowed_hosts:
        try:
            result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise ValueError('Ping failed') from e
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    response = secure_ping(host)
    return {'status': 'completed', 'output': response}