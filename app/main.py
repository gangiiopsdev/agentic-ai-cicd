from fastapi import FastAPI
import re
import shlex

app = FastAPI()

def execute_ping(host):
    # Regular expression to validate the host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host format')
    result = subprocess.run(['ping', '-c', '1'] + shlex.split(host), capture_output=True, text=True, check=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    response = execute_ping(host)
    return {'status': 'completed', 'output': response}