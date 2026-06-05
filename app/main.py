from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run_command(command, *args):
        safe_args = [subprocess.list2cmdline(arg) for arg in args]
        return subprocess.run([command] + safe_args, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    SafeSubprocess.run_command('ping', host)
    return {"status": "completed"}