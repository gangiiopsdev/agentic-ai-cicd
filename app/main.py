from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Basic validation to ensure the host does not contain potentially harmful characters
    return all(c.isalnum() or c in ('.', '-', '_') for c in host)

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'invalid input'}
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}