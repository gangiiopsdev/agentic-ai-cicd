from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def safe_run(command, *args, **kwargs):
        args = shlex.split(command)
        subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Use parameterized command to avoid injection
    command = 'ping -c 1 {host}'
    SafeSubprocess.safe_run(command.format(host=shlex.quote(host)))
    return {"status": "completed"}