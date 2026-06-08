from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return False
    safe_hosts = ['example.com', 'test.com']
    return host in safe_hosts

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid or unallowed host input'}, 400

    # Execute the ping command safely using subprocess.Popen
    process = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode != 0:
        return {'error': 'Ping failed'}, 500

    return {'status': 'completed', 'output': output.decode()}