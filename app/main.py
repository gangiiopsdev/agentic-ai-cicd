from fastapi import FastAPI
import subprocess
import shlex

def ping(host: str):
    try:
        # Validate the host input
        if not all(c in string.ascii_letters + string.digits for c in host):
            return {'status': 'failed', 'error': 'Invalid input'}
        
        # Using check_output to avoid shell=True and capture output
        result = subprocess.check_output(shlex.split(f'ping {host}'), stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': result.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

app = FastAPI()

@app.get("/ping")
def ping_wrapper(host: str):
    return ping(host)