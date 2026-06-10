from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        safe_host = host.replace(';', '').replace('&', '').replace('`', '').replace('$', '').replace('{', '').replace('}', '').replace('|', '').replace('\', '').replace('^', '').replace('~', '')  # Enhanced input sanitization
        try:
            output = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_wrapper(host: str):
    safe_pinger = SafePing()
    return safe_pinger.ping(host)