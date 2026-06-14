from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Validate input to prevent command injection
    if not host.strip() or '&&' in host or ';' in host or '|' in host:
        raise ValueError('Invalid host parameter')
    try:
        cmd = ['ping', shlex.quote(host)]
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {
            "status": "completed",
            "stdout": result.stdout.decode(),
            "stderr": result.stderr.decode()
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "error",
            "stdout": str(e),
            "stderr": str(e)
        }

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)