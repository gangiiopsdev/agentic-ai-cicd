from fastapi import FastAPI
import subprocess
def run_command(command):
    return subprocess.run(command, capture_output=True, text=True)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    command = ['ping', host]
    result = run_command(command)
    return {'status': 'completed'}