from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    # Safe implementation without shell=True
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def ping(host: str):
    if not host or ' ' in host:
        raise ValueError('Invalid input for host')
    result = execute_ping(host)
    return {'status': 'completed', 'result': result}