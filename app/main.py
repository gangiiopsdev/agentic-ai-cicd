from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']  # Add allowed hosts here
    return host in allowed_hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        command = subprocess.Popen(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = command.communicate()
        return {'status': 'completed', 'output': output.decode(), 'error': error.decode()}
    else:
        return {'error': 'Invalid host'}