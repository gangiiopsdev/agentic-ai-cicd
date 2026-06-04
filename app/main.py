from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run(command: list, *args, **kwargs):
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

def is_valid_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Add other allowed hosts as needed
    return host in allowed_hosts

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}, 400
    # Secure implementation using SafeSubprocess.run
    output = SafeSubprocess.run(['ping', host])
    return {'status': 'completed', 'output': output}