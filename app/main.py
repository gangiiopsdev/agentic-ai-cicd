from fastapi import FastAPI
import subprocess
def execute_ping(host):
    # Safe implementation using subprocess.Popen with proper sanitization
    args = ['ping', '-c', '1', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode('utf-8'), stderr.decode('utf-8')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    stdout, stderr = execute_ping(host)
    return {'status': 'completed', 'stdout': stdout, 'stderr': stderr}