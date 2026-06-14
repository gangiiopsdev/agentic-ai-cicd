from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_ping(host: str):
    try:
        result = subprocess.run(shlex.split('ping ' + host), check=True, stdout=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e}', 400

def validate_host(host: str):
    allowed_hosts = ['example.com', '127.0.0.1']  # Add more valid hosts here
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    return execute_ping(host)