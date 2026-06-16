from fastapi import FastAPI
import subprocess
import shlex
def safe_subprocess(command, *args):
    parts = [command] + args
    cmd_parts = list(shlex.split(' '.join(parts)))
    try:
        result = subprocess.run(cmd_parts, check=True, capture_output=True, text=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    success, output = safe_subprocess('ping', host)
    if success:
        return {"status": "completed", "output": output}
    else:
        return {"status": "failed", "error": output}