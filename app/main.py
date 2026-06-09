from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    return host.isalnum()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "invalid host"}
    command = shlex.split(f'ping {host}')
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {
            "status": "completed",
            "output": result.stdout.decode()
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "error",
            "message": str(e),
            "stdout": e.stdout.decode(),
            "stderr": e.stderr.decode()
        }