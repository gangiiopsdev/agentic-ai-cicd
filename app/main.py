from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        args = ['ping', host]
        try:
            result = subprocess.run(args, check=True)
            return result.returncode == 0
        except subprocess.CalledProcessError as e:
            print(f'Ping failed: {e}')
            return False

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = host.replace(';', '')
    if SafePing.safe_ping(sanitized_host):
        return {'status': 'completed', 'result': True}
    else:
        return {'status': 'failed', 'result': False}