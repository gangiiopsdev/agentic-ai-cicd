from fastapi import FastAPI
import subprocess
import shlex

global host_list
host_list = ['example.com', 'test.com']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host not in host_list:
        return {'status': 'error', 'result': 'Invalid host'}
    try:
        cmd = ['ping'] + shlex.split(host)
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'result': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return str(e.output.decode('utf-8'))