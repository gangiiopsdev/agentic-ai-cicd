from fastapi import FastAPI
import shlex
import os

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Host is not allowed')

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        command = ['ping', shlex.quote(host)]
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    else:
        return {'status': 'failed', 'error': 'Host is not allowed'}

# Add additional security measures
if __name__ == '__main__':
    import uvicorn
    # Bind to a specific IP address instead of all interfaces
    uvicorn.run(app, host='127.0.0.1', port=80)