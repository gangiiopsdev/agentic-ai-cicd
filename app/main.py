from fastapi import FastAPI
import subprocess
getpass = __import__('getpass')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host or not isinstance(host, str) or len(host.split('.')) != 4:
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}