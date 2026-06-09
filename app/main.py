from fastapi import FastAPI
import shlex
import subprocess
def sanitize_input(input_str):
    if 'ping' in input_str:
        return None
    return input_str
def escape_shell_arg(arg):
    return shlex.quote(arg)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if sanitized_host is not None:
        subprocess.call(['ping', escape_shell_arg(sanitized_host)], shell=False)
    else:
        return {"error": "Invalid input"}

    return {"status": "completed"}