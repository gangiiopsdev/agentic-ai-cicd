from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(user_input):
    return ''.join(c for c in user_input if c.isalnum() or c.isspace())
def escape_shell_args(args):
    return [shlex.quote(arg) for arg in args]
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ['ping', *escape_shell_args(sanitized_host)]
    try:
        result = subprocess.run(command, check=True, shell=False, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}