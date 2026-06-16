from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def ping(host: str):
        try:
            output = subprocess.check_output(['ping', *shlex.split(host)], stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_handler(host: str):
    sanitized_host = shlex.quote(host)
    return SafeSubprocess.ping(sanitized_host)