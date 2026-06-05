from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess_call(args):
    # Use shlex to safely split command arguments
    try:
        args = shlex.split(' '.join(args))
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get('/ping')
def ping(host: str):
    safe_host = ''.join(c for c in host if c.isalnum() or c in ('.', '-'))
    return safe_subprocess_call(['ping', safe_host])