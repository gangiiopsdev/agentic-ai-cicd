from fastapi import FastAPI
import subprocess
import shlex
def escape_shell_argument(argument):
    return shlex.quote(argument)

class SafePing:
    @staticmethod
def safe_ping(host: str) -> dict:
        if not host or not isinstance(host, str):
            return {'status': 'error', 'output': 'Invalid host'}
        escaped_host = escape_shell_argument(host)
        command = ['ping', '-c', '4', escaped_host]
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'output': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return SafePing.safe_ping(host)