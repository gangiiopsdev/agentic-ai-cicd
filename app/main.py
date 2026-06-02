from fastapi import FastAPI
import subprocess
import shlex
class SanitizedSubprocess:
    @staticmethod
def run(command: str, *args, **kwargs):
        args = shlex.split(args[0]) if isinstance(args, tuple) and len(args) == 1 else list(args)
        return subprocess.run([command] + args, capture_output=True, text=True)

app = FastAPI()
def ping(host: str):
    # Secure implementation using subprocess.run
    if not host.isalnum():
        raise ValueError('Invalid host name')
    SanitizedSubprocess.run('ping', shlex.quote(host))
@app.get("/ping")
def ping_route(host: str):
    result = ping(host)
    return {'status': 'completed', 'output': result.stdout}