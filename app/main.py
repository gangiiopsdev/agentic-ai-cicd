from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    try:
        args = ['ping', host]
        output = subprocess.run(args, capture_output=True, text=True, timeout=5)
        return output.stdout.strip()
    except subprocess.CalledProcessError as e:
        return str(e.stderr.strip())

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = safe_ping(shlex.quote(host))
    return {'status': 'completed', 'result': result}