from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    if not isinstance(arg, str):
        arg = str(arg)
    return subprocess.list2cmdline([arg])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        output = subprocess.check_output(['ping', escape_shell_arg(host)], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}
    except subprocess.TimeoutExpired:
        return {"status": "timeout", "error": "Command timed out"}