from fastapi import FastAPI
import subprocess
import shlex
import os

class SafeProcess:
    @staticmethod
    def safe_subprocess(command, *args):
        if isinstance(command, str):
            command = shlex.split(command)
        for arg in args:
            if isinstance(arg, list):
                command.extend(arg)
            else:
                command.append(arg)
        return command

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda x: x in allowed_chars, input_str))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = SafeProcess.safe_subprocess(['ping', *shlex.split(sanitized_host)])
    subprocess.run(command, check=True)
    return {"status": "completed"}