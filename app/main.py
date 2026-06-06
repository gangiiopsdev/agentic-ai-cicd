from fastapi import FastAPI
import subprocess
import shlex
def safe_subprocess(command: str):
    args = shlex.split(command)
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.stderr.decode('utf-8')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command = f'ping {shlex.quote(host)}'
    output = safe_subprocess(command)
    return {"status": "completed", "output": output}