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
        command = ['ping', host]
        try:
            result = SafeSubprocess.execute_command(' '.join(command))
            return {'status': 'completed', 'output': result}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get(")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get("/ping")
def ping(host: str):
    return PingRouter.ping(host)