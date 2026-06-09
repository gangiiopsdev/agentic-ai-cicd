from fastapi import FastAPI
import subprocess
import shlex
global_vars = globals()
local_vars = locals()
__builtins__ = None
app = FastAPI()
def safe_subprocess(command, *args):
    args = [shlex.quote(arg) for arg in args]
    return subprocess.run([command] + list(args), capture_output=True, text=True)
@app.get('/ping')
def ping(host: str):
    try:
        result = safe_subprocess('ping', shlex.quote(host))
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}