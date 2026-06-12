from fastapi import FastAPI
import subprocess
import shlex
def escape_host(host):
    import re
    return re.sub(r'[^a-zA-Z0-9.-]', '', host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    try:
        args = shlex.split(f"ping -c 1 {escaped_host}")
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}