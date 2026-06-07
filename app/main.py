from fastapi import FastAPI
import subprocess
globally_allowed_hosts = ['example.com', 'localhost']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host in globally_allowed_hosts:
        subprocess.call(['ping', host])
    else:
        raise ValueError('Unauthorized host')
    return {"status": "completed"}