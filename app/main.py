from fastapi import FastAPI
import subprocess

app = FastAPI()

async def run_ping(host):
    try:
        # Validate host input to avoid injection attacks
        if not host.isdigit():
            raise ValueError("Invalid host format")
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
        return stdout.decode() or stderr.decode()
    except (subprocess.CalledProcessError, ValueError) as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return run_ping(host)