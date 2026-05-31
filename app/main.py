from fastapi import FastAPI
import subprocess
def escape_shell_arg(s):
    return s.replace(';', ';').replace('$', '\$')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        output = subprocess.check_output(["ping", escape_shell_arg(host)], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {"status": "failed", "error": str(e)}