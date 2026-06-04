from fastapi import FastAPI
import subprocess
from shlex import quote
def escape_shell_arg(arg):
    return ' '.join(quote(a) for a in arg.split())

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_shell_arg(host)
    try:
        result = subprocess.run(['ping', '-c', '1'] + quote(escaped_host).split(), check=True, capture_output=True, text=True)
        return {"status": "completed", "stdout": result.stdout, "stderr": result.stderr}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}