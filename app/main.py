from fastapi import FastAPI
import subprocess

class SafeSubprocess:
    @staticmethod
def ping(host: str):
        try:
            # Validate and sanitize the host input
            if not host.replace('.', '').isdigit():
                raise ValueError('Invalid host format')
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return SafeSubprocess.ping(host)