from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run(command):
        return subprocess.run(command, capture_output=True, text=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    safe_command = ['ping', host]
    result = SafeSubprocess.run(safe_command)
    return {'status': 'completed', 'output': result.stdout}