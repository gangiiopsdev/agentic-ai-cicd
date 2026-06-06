from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def safe_ping(host: str):
        try:
            result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return e.stderr

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the input to prevent command injection
    if not all(c.isalnum() for c in host) or len(host) > 15:
        return {'error': 'Invalid host input'}
    # Sanitize the input using a whitelist approach
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        return {'error': 'Host is not allowed'}
    return {'status': SafeSubprocess.safe_ping(host)}