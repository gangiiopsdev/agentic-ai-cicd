from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def call(command: str):
        args = shlex.split(command)
        subprocess.call(args, shell=False)

app = FastAPI()

def validate_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(char in allowed_chars for char in input_string)

@app.get("/ping")
def ping(host: str):
    if not validate_input(host):
        raise ValueError('Invalid input detected')
    SafeSubprocess.call(f'ping {host}')
    return {"status": "completed"}