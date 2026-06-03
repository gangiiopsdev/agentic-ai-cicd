from fastapi import FastAPI
import subprocess
import shlex

host_list = ['127.0.0.1', '::1']

app = FastAPI()

def ping(host: str):
    if host in host_list:
        try:
            result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}