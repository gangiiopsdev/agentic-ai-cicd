from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        # Secure implementation with validation and sanitization
        valid_hosts = ['example.com', 'google.com']
        if host not in valid_hosts:
            return {'status': 'failed', 'error': 'Invalid host'}
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping_endpoint(host: str):
    return SafeSubprocess.ping(host)