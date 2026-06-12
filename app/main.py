from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run(command: str, *args, **kwargs):
        args = [shlex.quote(arg) for arg in command.split()]
        try:
            result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, *args, **kwargs)
            return result.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return str(e.stderr.decode('utf-8'))

app = FastAPI()
def safe_ping(host: str):
    command = f'ping {shlex.quote(host)}'
    return SafeSubprocess.run(command)

@app.get("/ping")
def ping(host: str):  # Validate input
    if not host.isalnum():
        raise ValueError('Invalid host name')
    return safe_ping(host)