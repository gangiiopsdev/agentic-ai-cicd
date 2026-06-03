from fastapi import FastAPI
import subprocess
def validate_host(host):
    if not host.isalnum() or len(host) > 100:
        raise ValueError('Invalid host name')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        validate_host(host)
        result = subprocess.run(['ping', '-c', '1'], capture_output=True, text=True, check=True, input=host, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}