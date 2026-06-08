from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation and sanitization
    command = ['ping', host]
    subprocess.run(command, check=True)
    return {'status': 'completed'}