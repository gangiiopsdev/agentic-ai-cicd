from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    if not host or len(host) > 255:
        raise ValueError("Invalid host")
    return host

@app.get("/ping")
def ping(host: str):
    validated_host = validate_host(host)
    command = ['ping', '-c', '1', shlex.quote(validated_host)]
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": e.stderr.decode()}