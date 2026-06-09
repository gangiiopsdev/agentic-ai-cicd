from fastapi import FastAPI
import subprocess

app = FastAPI()
allowed_hosts = ['example.com', 'localhost']

@app.get("/ping")
def ping(host: str):
    if host in allowed_hosts:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'error': 'Invalid host'}