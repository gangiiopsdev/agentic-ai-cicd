from fastapi import FastAPI
import subprocess
import shlex
def _ping(host):
    try:
        # Validate and sanitize the host input
        if not host.isalnum():
            raise ValueError("Invalid host")
        cmd = ['ping', '-c', '1'] + shlex.split(host)
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        return True, output.decode('utf-8')
    except (subprocess.CalledProcessError, ValueError) as e:
        return False, str(e.output)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    success, result = _ping(host)
    if success:
        return {"status": "completed", "message": "Ping successful", "output": result}
    else:
        return {"status": "failed", "error": result}