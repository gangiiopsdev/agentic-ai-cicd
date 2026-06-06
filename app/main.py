from fastapi import FastAPI
import subprocess
from shlex import quote

class SafeSubprocess:
    @staticmethod
def safe_run(command):
        # Sanitize the command arguments
        sanitized_command = [quote(arg) for arg in command]
        result = subprocess.run(sanitized_command, capture_output=True, text=True, check=True)
        return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = ['ping', host]
    response = SafeSubprocess.safe_run(command)
    return {'status': 'completed', 'response': response}