from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Secure implementation using safe methods
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, universal_newlines=True)
            return {'output': output}
        except subprocess.CalledProcessError as e:
            return {'error': e.output}

global_ping = SafePing.safe_ping

app = FastAPI()

@app.get('/ping')
def ping_safe(host: str):
    return global_ping(host)