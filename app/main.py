from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if 'ping' in host:
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.call(['ping', subprocess.check_output('hostname').decode().strip()], shell=False)
    return {'status': 'completed'}