from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_safe_command(command):
    return subprocess.run(command, shell=False, check=True)

@app.get("/ping")
def ping(host: str):
    command = ['ping', host]
    result = run_safe_command(command)
    return {'status': 'completed'}