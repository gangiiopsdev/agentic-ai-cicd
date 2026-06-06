from fastapi import FastAPI
import subprocess
from shlex import quote
from typing import List, Tuple

app = FastAPI()
def execute_command(command: str, arguments: List[str]) -> Tuple[str, str]:
    sanitized_arguments = [quote(arg) for arg in arguments]
    process = subprocess.Popen([command] + sanitized_arguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    output, error = process.communicate()
    return output.decode(), error.decode().replace('\n', '\n')

@app.get("/ping")
def ping(host: str) -> dict:
    try:
        sanitized_host = quote(host)
        output, _ = execute_command('ping', [sanitized_host])
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}