from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(char in allowed_chars for char in host)
class SafeSubprocess:
    @staticmethod
def safe_subprocess_call(command_parts):
        command = ' '.join(shlex.quote(arg) for arg in command_parts)
        subprocess.run(command, shell=False, executable='/bin/sh', check=True, capture_output=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        command_parts = ["ping", host]
        SafeSubprocess.safe_subprocess_call(command_parts)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}