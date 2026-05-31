from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run(command: str, *args, **kwargs):
        try:
            result = subprocess.run(command.split(), check=True, *args, **kwargs)
            return result.stdout.decode()
        except subprocess.CalledProcessError as e:
            return f'Error: {e.stderr.decode()}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_command = shlex.split(f'ping -c 1 {host}')
    return SafeSubprocess.run(safe_command)