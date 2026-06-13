from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def safe_ping(host):
    try:
        args = shlex.split('ping ' + host)
        result = await asyncio.create_subprocess_exec(*args, check=True, capture_output=True)
        return {"status": "completed", "stdout": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

@app.get("/ping")
def ping(host: str):
    return asyncio.run(safe_ping(host))