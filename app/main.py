from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c in ' .-')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    try:
        args = ['ping', shlex.quote(host)]
        subprocess.run(args, check=True, shell=False)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}