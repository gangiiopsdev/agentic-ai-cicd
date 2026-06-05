from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def safe_subprocess_call(command_parts):
        command = ' '.join(shlex.quote(arg) for arg in command_parts)
        return subprocess.run(command, shell=False, executable='/bin/sh', check=True, capture_output=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command_parts = ["ping", host]
    SafeSubprocess.safe_subprocess_call(command_parts)
    return {"status": "completed"}