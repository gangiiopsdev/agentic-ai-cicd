from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_ping(host):
    try:
        # Use shlex.quote to safely escape the host parameter
        safe_host = shlex.quote(host)
        result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    output = execute_ping(host)
    return {'status': 'completed', 'output': output}