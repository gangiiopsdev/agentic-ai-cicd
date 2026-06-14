from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    args = ['ping', host]
    # Ensure that the arguments are properly quoted and escaped
    cmd = ' '.join(shlex.quote(arg) for arg in args)
    # Use subprocess.run to execute the command safely
    result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode()

@app.get("/ping")
def ping(host: str):
    try:
        output = safe_ping(host)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}