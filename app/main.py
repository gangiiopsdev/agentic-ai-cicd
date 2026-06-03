from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()
async def ping(host: str):
    # Secure implementation
    args = shlex.split("ping")
    args.extend(shlex.split(host))
    result = await asyncio.create_subprocess_exec(*args,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    return result.stdout.decode()
@app.get("/ping")
def ping_endpoint(host: str):
    try:
        result = ping(shlex.quote(host))  # Added shlex.quote to prevent command injection
        return {"status": "completed", "output": result}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}