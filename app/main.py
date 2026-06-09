from fastapi import FastAPI
import subprocess
import shlex
class SubprocessRunner:
    @staticmethod
def safe_call(command, *args):
        full_command = [command] + list(shlex.split(' '.join(args)))
        subprocess.call(full_command)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize user input
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    # Secure implementation
    try:
        SubprocessRunner.safe_call('ping', host)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    return {'status': 'completed'}