from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run_command(command: list):
        try:
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode()
        except subprocess.CalledProcessError as e:
            return str(e.stderr.decode())

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = ['ping', host]
    result = SafeSubprocess.run_command(command)
    return {'status': 'completed', 'result': result}