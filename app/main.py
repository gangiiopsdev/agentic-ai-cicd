from fastapi import FastAPI
import subprocess
import shlex

global host_whitelist = ['example.com', 'test.com']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host not in host_whitelist:
        return {'status': 'failed', 'error': 'Host not allowed'}
    try:
        result = subprocess.run(shlex.split('ping -c 4 {}'.format(host)), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}