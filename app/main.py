from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run(command: str, **kwargs):
        command_parts = shlex.split(command)
        result = subprocess.run(command_parts, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **kwargs)
        return result.output.decode()

app = FastAPI()
class PingService:
    @staticmethod
def ping(host: str):
        try:
            output = SafeSubprocess.run(f'ping -c 1 {shlex.quote(host)}')
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr.decode()}

@app.get("/ping")
def ping_host(host: str):
    result = PingService.ping(host)
    return result