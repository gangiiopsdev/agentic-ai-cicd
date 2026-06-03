from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def execute_command(command):
        args = shlex.split(command)
        try:
            result = subprocess.run(args, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)
class PingRouter:
    @staticmethod
def ping(host: str):
        command = f'ping {host}'
        try:
            result = SafeSubprocess.execute_command(command)
            return {'status': 'completed', 'output': result}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get("/ping")
def ping(host: str):
    if host.isalnum() or '.' in host and not '..' in host:
        return PingRouter.ping(host)
    else:
        return {'status': 'error', 'message': 'Invalid host'}