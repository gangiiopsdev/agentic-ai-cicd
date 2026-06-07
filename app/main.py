from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run_command(command, args):
        try:
            output = subprocess.check_output([command] + args, stderr=subprocess.STDOUT, universal_newlines=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_subprocess = SafeSubprocess()
    return safe_subprocess.run_command('ping', [host])