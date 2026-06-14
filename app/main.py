from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host):
    try:
        output = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await output.communicate()
        if output.returncode != 0:
            raise subprocess.CalledProcessError(output.returncode, 'ping', output.stderr.decode())
        return stdout.decode().strip()
    except (subprocess.CalledProcessError, asyncio.TimeoutError) as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    result = await safe_ping(host)
    return {"status": "completed", "result": result}