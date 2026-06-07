from fastapi import FastAPI
import subprocess
import shlex

def ping(host: str):
    try:
        output = subprocess.check_output(shlex.split('ping ' + host), stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    if not host.isalnum():
        return {'status': 'invalid', 'message': 'Invalid input'}
    try:
        # Validate and sanitize the input further if necessary
        subprocess.run(shlex.split('ping ' + host), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return ping(host)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode('utf-8')}