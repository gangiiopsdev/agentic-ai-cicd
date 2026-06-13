from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(user_input):
    return ''.join(e for e in user_input if e.isalnum() or e in ['-', '.', '_'])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {"status": "failed", "error": "Invalid input"}
    cmd = ['ping', '-c', '1', shlex.quote(sanitized_host)]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, universal_newlines=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}