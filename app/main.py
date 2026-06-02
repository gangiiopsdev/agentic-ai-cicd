from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    valid_hosts = ['example.com', 'localhost']
    if host in valid_hosts:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {'status': 'completed', 'result': response}