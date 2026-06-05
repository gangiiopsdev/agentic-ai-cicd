from fastapi import FastAPI
import subprocess
import shlex
def escape_shell_arg(arg):
    return arg.replace(';', ' ').replace('&', ' ').replace('$', '').replace('*', '')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_shell_arg(host)
    try:
        result = subprocess.run(['ping', '-c', '1'] + shlex.split(escaped_host), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "stdout": result.stdout.decode(), "stderr": result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

# Preventive controls:
# - Use parameterized queries or prepared statements for database operations.
# - Validate and sanitize all user inputs before using them in shell commands.
# - Limit the set of allowed commands or options that can be executed through subprocess calls.