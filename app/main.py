from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def safe_ping(host: str):
        args = ['ping', host]
        # Use subprocess.run instead of subprocess.call for better security and error handling
        result = subprocess.run(args, capture_output=True, text=True)
        return result
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    result = SafePing.safe_ping(host)
    return {'status': 'completed', 'result': result.stdout}