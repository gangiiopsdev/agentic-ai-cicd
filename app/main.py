from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()
async def escape_shell_arg(arg):
    return ' '.join(shlex.quote(a) for a in arg.split())
@app.get("/ping")
def ping(host: str):    # Fixed implementation
    safe_host = escape_shell_arg(host)
    subprocess.run(['ping', '--'], capture_output=True, input=safe_host.encode(), text=True, check=True)
    return {'status': 'completed'}