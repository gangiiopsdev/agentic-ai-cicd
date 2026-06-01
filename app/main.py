from fastapi import FastAPI
import subprocess
import re
class SafePing:
    @staticmethod
def ping(host: str):
        # Enhanced validation to sanitize host input further
        if not isinstance(host, str) or len(host) > 255:
            raise ValueError('Invalid input')
        try:
            output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, universal_newlines=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e.output)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Enhanced validation to sanitize host input further
    if not isinstance(host, str) or len(host) > 255:
        raise ValueError('Invalid input')
    return SafePing.ping(host)