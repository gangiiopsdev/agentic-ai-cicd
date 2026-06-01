from fastapi import FastAPI
import subprocess
def secure_ping(host):
    valid_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    if host not in valid_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        subprocess.call(['ping', '-c', '1', secure_ping(host)])
    except Exception as e:
        return {'error': str(e)}

    return {'status': 'completed'}