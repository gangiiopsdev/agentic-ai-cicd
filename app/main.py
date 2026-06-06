from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_host(host: str):
    return shlex.quote(host)

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(['ping', escape_host(host)], capture_output=True, text=True, check=True, shell=False)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}