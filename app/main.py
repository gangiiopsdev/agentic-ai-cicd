from fastapi import FastAPI
import shlex

app = FastAPI()

async def execute_ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or len(host) > 64:
        return False
    try:
        cmd = ['ping'] + shlex.split(shlex.quote(host))
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError as e:
        return False

@app.get("/ping")
def ping(host: str):
    return await execute_ping(host)