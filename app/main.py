from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host):
        allowed_hosts = ['example.com', 'test.com']  # Add more valid hosts as needed
        if host not in allowed_hosts:
            raise ValueError('Invalid host')
        try:
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return SafeSubprocess.ping(host)