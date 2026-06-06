from fastapi import FastAPI
import subprocess
import shlex
from typing import List

def sanitize_input(input_str: str) -> str:
    return input_str.replace(';', '').replace('&', '')

app = FastAPI()
def execute_command(command: str, arguments: List[str]) -> Tuple[bytes, bytes]:
    sanitized_arguments = [shlex.quote(arg) for arg in arguments]
    process = subprocess.Popen([command] + sanitized_arguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    output, error = process.communicate()
    return output, error

@app.get("/ping")
def ping(host: str):
    try:
        host = sanitize_input(host)
        output, _ = execute_command('ping', [host])
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}