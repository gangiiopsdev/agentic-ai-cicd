from fastapi import FastAPI
import subprocess
gensh = lambda s: ''.join(c if c not in ';$' else '\' + c for c in s)
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.check_output(["ping", gensh(host)], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {"status": "failed", "error": str(e)}