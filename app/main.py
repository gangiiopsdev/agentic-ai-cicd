from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        args = ['ping', shlex.quote(host)]
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)