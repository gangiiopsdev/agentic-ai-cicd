from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    if not host.isalnum() or len(host) > 64:
        raise ValueError("Invalid input for host")
app = FastAPI()
@app.get('/ping')
def ping(host: str):    try:
        args = shlex.split(f'ping {host}')
        subprocess.call(args, shell=False)
    except Exception as e:
        return {"error": str(e)}
    return {"status": "completed"}
# Fixed by sanitizing the host input before passing it to subprocess
@app.get('/ping_fixed')
def ping_fixed(host: str):    try:
        if not host.isalnum() or len(host) > 64:
            raise ValueError("Invalid input for host")
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"error": str(e)}