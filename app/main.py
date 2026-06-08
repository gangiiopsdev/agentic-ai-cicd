from fastapi import FastAPI
import subprocess
class CommandExecution:
    @staticmethod
def safe_ping(host: str) -> bool:
        try:
            result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return True, result.stdout.decode()
        except subprocess.CalledProcessError as e:
            return False, e.stderr.decode()

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    is_successful, output = CommandExecution.safe_ping(host)
    return {'status': 'completed', 'is_successful': is_successful, 'output': output}