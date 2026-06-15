from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    args = shlex.split('ping ' + host)
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_handler(host: str):
    try:
        ping(host)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}