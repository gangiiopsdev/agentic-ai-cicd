from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run(command: str, *args, **kwargs):
        args = [shlex.quote(arg) for arg in args]
        full_command = ' '.join([command] + list(args))
        return subprocess.run(full_command, capture_output=True, text=True, check=True)

app = FastAPI()
def _ping(host):
    # Validate input to prevent command injection
    if not host.isalnum():
        raise ValueError("Invalid host")
    try:
        response = SafeSubprocess.run('ping', host)
        return response.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    result = _ping(host)
    return {"status": "completed", "result": result}