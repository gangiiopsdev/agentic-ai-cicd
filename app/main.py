from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.isnumeric():
        subprocess.call(['ping', host])
    else:
        return {'status': 'Invalid input'}
    return {'status': 'completed'}