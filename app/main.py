from fastapi import FastAPI
import shlex
from subprocess import Popen, PIPE

def validate_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(char in allowed_chars for char in host)

class SafeSubprocess:
    @staticmethod
    def safe_subprocess_call(command_parts):
        command = ' '.join(shlex.quote(arg) for arg in command_parts)
        result = Popen(command, shell=False, executable='/bin/sh', check=True, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        command_parts = ["ping", host]
        output = SafeSubprocess.safe_subprocess_call(command_parts)
        return {"status": "completed", "output": output}
    else:
        return {"error": "Invalid host"}