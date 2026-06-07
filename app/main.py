from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    try:
        cmd = shlex.split(f"ping {host}")
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}
    except subprocess.TimeoutExpired:
        return {"status": "timed out"}

app.get("/")(home)
app.get("/ping")(ping)