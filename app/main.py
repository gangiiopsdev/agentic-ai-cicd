from fastapi import FastAPI
import subprocess
global host_list
host_list = ['127.0.0.1', '::1']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host in host_list:
        try:
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        raise Exception('Invalid host')