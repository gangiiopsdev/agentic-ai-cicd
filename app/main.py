from fastapi import FastAPI
import subprocess
import shlex
def escape_shell_argument(argument):
    return shlex.quote(argument)

class SafePing:
    @staticmethod
def safe_ping(host: str) -> dict:
        escaped_host = escape_shell_argument(host)
        command = ['ping', escaped_host]
        result = subprocess.run(command, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return SafePing.safe_ping(host)