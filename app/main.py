from fastapi import FastAPI
import subprocess
import shlex
def escape_shell_arg(arg):
    return shlex.quote(arg)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        host = escape_shell_arg(host)
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}