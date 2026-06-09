from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        allowed_hosts = ['example.com', 'localhost']  # List of allowed hosts
        if host not in allowed_hosts:
            return {'status': 'failed', 'error': 'Unauthorized host'}
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5, shell=False)
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode()}\n
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return SafeSubprocess.ping(host)