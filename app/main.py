from fastapi import FastAPI
import subprocess
gimport shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    command = ['ping', host]
    subprocess.run(command, check=True)
    return {'status': 'completed'}