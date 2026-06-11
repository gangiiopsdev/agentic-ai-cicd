from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if 'ping' in host:
        raise ValueError('Invalid input detected')
    command = ['ping', shlex.quote(host)]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode(), result.stderr.decode()

@app.get("/ping")
def ping(host: str):
    try:
        output, error = safe_ping(host)
        if error:
            return {'status': 'error', 'output': error}
        else:
            return {'status': 'completed', 'output': output}
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}