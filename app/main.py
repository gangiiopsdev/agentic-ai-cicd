from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Validate and sanitize the host input to prevent injection attacks
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            return 'Invalid host'
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return f'Error pinging {host}: {e.stderr}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_wrapper(host: str):
    result = SafePing.ping(host)
    return {'status': 'completed', 'result': result}