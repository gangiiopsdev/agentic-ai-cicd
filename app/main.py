from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5, shell=False)
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    if not all(c.isalnum() or c in ('.', '-') for c in host):  # Simple validation of hostname characters
        return {'status': 'failed', 'error': 'Invalid host name'}
    return SafeSubprocess.ping(host)