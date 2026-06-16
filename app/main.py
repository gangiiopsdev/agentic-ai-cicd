from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host in allowed_hosts:
        try:
            result = subprocess.run(['ping', '-c', '4', host], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e)}
    else:
        return {'status': 'error', 'message': 'Invalid host'}