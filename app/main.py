from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Safer implementation using shlex to escape arguments and subprocess.run for better control
    command = ['ping', host]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return {'result': result.stdout}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)