from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use shlex.quote to safely handle user input
        cmd = ['ping', shlex.quote(host)]
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    if isinstance(output, str) and 'command not found' in output:
        return {'status': 'failed', 'error': 'Invalid command'}
    else:
        return {'status': 'completed', 'output': output}