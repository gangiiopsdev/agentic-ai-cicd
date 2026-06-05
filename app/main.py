from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        if not host.isalnum():
            raise ValueError('Invalid hostname')
        args = ['ping', host]
        result = subprocess.run(args, shell=False, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        return SafePing.safe_ping(host)
    except ValueError as e:
        return {'error': str(e)}, 400