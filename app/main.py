from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', 'localhost']  # Add your allowed hosts here
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    try:
        subprocess.check_call(['ping', host], shell=False, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return False, str(e)
    return True, 'completed'

@app.get("/ping")
def ping(host: str):
    result, message = safe_ping(host)
    if result:
        return {'status': 'completed'}
    else:
        return {'status': 'failed', 'error': message}