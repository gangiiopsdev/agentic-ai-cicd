from fastapi import FastAPI
import subprocess
import shlex
def _ping(host):
    try:
        cmd = ['ping', '-c', '1'] + shlex.split(host)
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        return True, output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return False, str(e.output)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    success, result = _ping(host)
    if success:
        return {"status": "completed", "message": "Ping successful", "output": result}
    else:
        return {"status": "failed", "error": result}