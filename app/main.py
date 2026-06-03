from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run(command, *args, **kwargs):
        command = shlex.split(command)
        return subprocess.run(command, check=True, *args, **kwargs)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    safe_host = SafeSubprocess.run(f'ping {host}', capture_output=True, text=True)
    return {'status': 'completed', 'output': safe_host.stdout}