from fastapi import FastAPI
import subprocess

app = FastAPI()

def get_host_from_safe_source():
    # Securely obtain the host from a safe source
    return 'example.com'

@app.get('/ping')
def ping():
    host = get_host_from_safe_source()
    glances = ['ping', host]
    subprocess.call(glances, shell=False)
    return {'status': 'completed'}