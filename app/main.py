from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    try:
        args = ['ping'] + [arg for arg in shlex.split(host) if arg.isalnum()]
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if 'error' in result:
        return result
    else:
        return result