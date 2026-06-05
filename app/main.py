from fastapi import FastAPI
import subprocess
from shlex import quote
from subprocess import Popen, PIPE

app = FastAPI()

def execute_command(command_parts):
    try:
        process = Popen(command_parts, stdout=PIPE, stderr=PIPE, text=True)
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            raise subprocess.CalledProcessError(process.returncode, ' '.join(command_parts), output=stderr)
        return stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    command_parts = ['ping', host]
    output = execute_command(command_parts)
    return {'status': 'completed', 'output': output}