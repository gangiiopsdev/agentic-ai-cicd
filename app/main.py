from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run_command(command: list):
        try:
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed', 'result': 'success', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'completed', 'result': 'failure', 'output': str(e.output)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_command = ['ping', host]
    return SafeSubprocess.run_command(safe_command)