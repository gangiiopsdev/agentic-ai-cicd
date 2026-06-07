from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        command = ['ping'] + shlex.split(host)
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping_safe(host: str):
    return SafeSubprocess.ping(host)