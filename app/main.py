from fastapi import FastAPI
import subprocess
import shlex
class SafeCommandRunner:
    def run(self, command_parts):
        try:
            result = subprocess.run(command_parts, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'output': e.stderr.decode()}

app = FastAPI()

def ping_safe(host: str):
    command_parts = ['ping', shlex.quote(host)]
    runner = SafeCommandRunner()
    return runner.run(command_parts)

@app.get("/ping")
def ping(host: str):
    return ping_safe(host)