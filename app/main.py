from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation using a whitelist of allowed hosts
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        args = ['ping', host]
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    else:
        return {'status': 'error', 'message': 'Host not allowed'}, 403