from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    args = ['ping', *shlex.split(host)]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, str(e)

@app.get("/ping")
def ping(host: str):
    success, output = safe_ping(host)
    if success:
        return {"status": "completed", "output": output}
    else:
        return {"status": "failed", "error": output}