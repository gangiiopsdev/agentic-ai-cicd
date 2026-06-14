from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.Popen and shlex
    cmd = ['ping', host]
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = popen.communicate()
    if popen.returncode != 0:
        raise Exception(f'Subprocess returned non-zero exit code: {popen.returncode}
{stderr.decode()}')

@app.get("/ping")
def ping_route(host: str):
    # Sanitize the host input to prevent command injection
    sanitized_host = shlex.quote(host)
    return ping(sanitized_host)