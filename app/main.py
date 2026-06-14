from fastapi import FastAPI
import subprocess
import shlex
def safe_command(*args):
    return ' '.join(shlex.quote(a) for a in args)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}