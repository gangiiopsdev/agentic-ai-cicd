from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_input(input_string):
    return quote(input_string)

def execute_command(command, *args):
    cmd = [command] + list(args)
    result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode(), result.stderr.decode()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    output, error = execute_command("ping", sanitized_host)
    if error:
        return {"status": "error", "message": error}
    else:
        return {"status": "completed", "output": output}