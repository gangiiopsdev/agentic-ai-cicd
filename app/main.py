from fastapi import FastAPI
import subprocess
import shlex

def execute_ping(host: str):
    try:
        args = shlex.split(f'ping {host}')
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.output}'

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not host or ' ' in host or '@' in host:
        return 'Invalid input'
    return execute_ping(host)