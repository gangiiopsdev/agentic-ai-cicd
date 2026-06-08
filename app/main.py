from fastapi import FastAPI
import subprocess
import shlex
global app 
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    command = ['ping', host]
    # Using subprocess.run with check=True and shell=False is safer than subprocess.call
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}