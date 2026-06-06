from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Sanitize input and safe implementation
    try:
        args = ['ping', host]
        sanitized_args = [shlex.quote(arg) for arg in args]
        output = subprocess.check_output(sanitized_args, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)