from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    try:
        args = ['ping', host]
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.output)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = safe_ping(shlex.quote(host))
    return {'status': 'completed', 'result': result}