from fastapi import FastAPI
import subprocess
def execute_ping(host):
    allowed_hosts = ['example.com', 'test.com']  # Add your list of allowed hosts here
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    try:
        output = subprocess.check_output(['ping', host], shell=False, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = execute_ping(host)
    return {'status': 'completed', 'result': result}