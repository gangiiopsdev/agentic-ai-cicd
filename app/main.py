from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ('.', '-', '_'))
def escape_shell_command(command, args):
    escaped_args = [shlex.quote(arg) for arg in args]
    return command + ' ' + ' '.join(escaped_args)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    escaped_command = escape_shell_command('ping', [sanitized_host])
    subprocess.run(escaped_command, check=True, shell=False, text=True)
    return {"status": "completed"}