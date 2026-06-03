from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def execute(command: str, *args: str):
        if not command.isalnum() or any(arg.isalnum() for arg in args):
            return {'error': 'Invalid input', 'status': 'failed'}
        full_command = [command] + [shlex.quote(arg) for arg in args]
        try:
            subprocess.run(full_command, check=True)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'error': str(e), 'status': 'failed'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return SafeSubprocess.execute('ping', host)