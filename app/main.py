from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Example allowed hosts list
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):

    if not validate_host(host):
        raise HTTPException(status_code=400, detail='Invalid host')

    # Safe implementation
    subprocess.call(['ping', host])

    return {'status': 'completed'}