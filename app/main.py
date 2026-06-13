from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run(command: list):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        if process.returncode != 0:
            raise Exception(f'Error running command: {error.decode()}')

app = FastAPI()

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
def ping(host: str):
    if host in ALLOWED_HOSTS:
        SafeSubprocess.run(['ping', '-c', '1', host])
    else:
        raise ValueError('Invalid host')

@app.get('/ping')
def ping_endpoint(host: str):
    try:
        response = ping(host)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}