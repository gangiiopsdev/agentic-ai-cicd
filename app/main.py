from fastapi import FastAPI
import subprocess
import shlex

def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and check=True
    try:
        result = subprocess.run(['ping'] + shlex.split(host), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.stderr.decode()}