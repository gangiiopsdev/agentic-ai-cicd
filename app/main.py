from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host):
        try:
            output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode()}

def safe_ping_decorator(func):
    def wrapper(host):
        return SafePing.safe_ping(host)
    return wrapper

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping_decorator(safe_ping)(host)