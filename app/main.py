from fastapi import FastAPI
import subprocess
import shlex

global host_whitelist = {'example.com', 'test.com'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input
    if host not in host_whitelist:
        return {'status': 'error', 'message': 'Invalid host'}
    
    # Secure implementation
    result = subprocess.run(['ping', '-c', '1'] + shlex.split(host), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}