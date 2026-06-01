from fastapi import FastAPI
import subprocess
import shlex
class CommandSanitizer:
    @staticmethod
def sanitize_command(command):
        return [shlex.quote(arg) for arg in command]

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.isalnum():
        raise ValueError('Invalid input, only alphanumeric characters are allowed')

    args = ['ping'] + CommandSanitizer.sanitize_command([host])
    subprocess.run(args, check=True)
    return {'status': 'completed'}