from fastapi import FastAPI
import re
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Validate and sanitize input
        if not re.match(r'^[a-zA-Z0-9,.!-_]{1,}$', host):
            raise ValueError('Invalid hostname')
        try:
            output = subprocess.run(['ping', '-c', '4', '--', host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_safe(host: str):
    result = SafePing.ping(host)
    return {'status': 'completed', 'result': result}