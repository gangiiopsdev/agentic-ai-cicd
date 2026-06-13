from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run_command(command, *args, **kwargs):
        full_command = [command] + list(args)
        full_command = [shlex.quote(arg) for arg in full_command]
        return subprocess.run(full_command, **kwargs)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize user input to prevent injection attacks
    if not host.isalnum():
        return {'status': 'error', 'output': 'Invalid input'}

    try:
        output = SafeSubprocess.run_command('ping', host, stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': output.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.output.decode('utf-8')}