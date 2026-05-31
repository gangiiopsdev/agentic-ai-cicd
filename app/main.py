from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    # Safe implementation
    try:
        args = ['ping', *shlex.split(host)]
        output = subprocess.run(args, check=True, capture_output=True, text=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}