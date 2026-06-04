from fastapi import FastAPI
import subprocess
import shlex

def is_valid_host(host: str) -> bool:
    # Basic validation for host input
    return host.strip() and '.' in host

platform = __import__('platform')
cmd = ['ping', '-c', '1'] if platform.system().lower() == 'linux' else ['ping', '-n', '1']
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate host input
    if not is_valid_host(host):
        return {"error": "Invalid host"}, 400
    args = cmd + [shlex.quote(host)]
    subprocess.call(args)
    return {"status": "completed"}