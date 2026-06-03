from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    command = ['ping'] + shlex.split(host)
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}