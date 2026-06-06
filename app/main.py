from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    @staticmethod
def execute(host: str):
        try:
            host = shlex.quote(host)
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, universal_newlines=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.strip()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():  # Add input validation to prevent command injection
        return {'status': 'failed', 'error': 'Invalid input'}
    return PingCommand.execute(host)