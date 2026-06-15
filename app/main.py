from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def execute_ping(host):
    try:
        args = ['ping', shlex.quote(host)]
        result = subprocess.run(args, capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)