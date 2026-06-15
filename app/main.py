from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and check=True
    try:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.stderr}