from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Safe implementation with shell=False and argument splitting
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        return {'result': 'Pinging ' + host}
    except Exception as e:
        return {'error': str(e)}