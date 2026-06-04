from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid input')
    subprocess.call(['ping', '-c', '1', host])  # Use specific command options to mitigate risks
    return {'status': 'completed'}