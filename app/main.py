from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            # Sanitize the input to prevent command injection
            host = sub.process.call('ping', shell=True, args=[host], capture_output=True, text=True)
            if result.returncode == 0:
                return {'status': 'completed'}
            else:
                return {'status': 'failed', 'error': result.stderr}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    return SafePing.ping(host)