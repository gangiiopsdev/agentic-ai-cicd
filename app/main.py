from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    try:
        args = ['ping', host]
        result = subprocess.run(shlex.split(' '.join(args)), check=True, capture_output=True, text=True)
        return {'status': 'Success', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'Failure', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)