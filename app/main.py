from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    try:
        args = ['ping', shlex.quote(host)]
        result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)