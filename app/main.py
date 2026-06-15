from fastapi import FastAPI
import subprocess
def execute_ping(host):
    try:
        output = subprocess.check_output(['ping', host], universal_newlines=True, shell=False)
        return output
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isdigit():
        return 'Invalid input'
    sanitized_host = subprocess.list2cmdline([host])
    return execute_ping(sanitized_host)