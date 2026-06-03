from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run(command, *args, **kwargs):
        if isinstance(command, str):
            command = shlex.split(command)
        return subprocess.run(command, *args, **kwargs)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Safe implementation
    safe_host = host.replace(';', '').replace('&', '').replace('\', '')
    command = ['ping', safe_host]
    result = SafeSubprocess.run(command)
    return {"status": "completed", "stdout": result.stdout.decode(), "stderr": result.stderr.decode()}