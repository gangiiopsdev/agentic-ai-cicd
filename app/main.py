from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def _ping(host):
    args = ['ping', shlex.quote(host)]
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr.decode('utf-8')}'

@app.get("/ping")
def ping(host: str):
    result = _ping(host)
    return {'status': 'completed', 'result': result}