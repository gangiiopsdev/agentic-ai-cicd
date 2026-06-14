from fastapi import FastAPI
import subprocess
import shlex

class Sanitize:
    @staticmethod
def safe_command(command):
        if not isinstance(command, str) or '&&' in command or '|' in command or ';' in command:
            raise ValueError('Invalid command')
        return command

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = Sanitize.safe_command(f'ping {shlex.quote(host)}')
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()
    return {'status': 'completed', 'output': output.decode()}