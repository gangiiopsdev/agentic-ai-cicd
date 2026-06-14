from fastapi import FastAPI
import subprocess
import shlex
def escape_shell_arg(arg):
    return shlex.quote(str(arg))

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        args = ['ping', escape_shell_arg(host)]
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

    return {'status': 'completed'}