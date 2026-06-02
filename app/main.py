from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Replace with safe method, e.g., using subprocess.run and avoiding shell=True
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
    if SafePing.safe_ping(host):
        return {'status': 'completed', 'result': True}
    else:
        return {'status': 'failed', 'result': False}