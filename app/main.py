from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def run(host):
        # Validate and sanitize the input to prevent command injection
        if not host.isalnum() or len(host) > 255:
            return 'Invalid host'
        try:
            result = subprocess.run(['ping', '"' + host + '"'], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

def shellquote(s):
    from pipes import quote
    return quote(s)

app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    return SafePing.run(shellquote(host))