from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_argument(arg):
    return arg.replace('`', '\\').replace('$', '\\$')

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with input validation and escaping
    if not host or len(host) > 255:
        raise ValueError("Invalid host")
    command = ['ping', '-c', '1', host]
    escaped_command = [escape_shell_argument(arg) for arg in command]
    result = subprocess.run(escaped_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "stdout": result.stdout.decode(), "stderr": result.stderr.decode()}