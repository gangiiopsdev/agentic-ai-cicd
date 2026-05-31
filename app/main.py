from fastapi import FastAPI
import subprocess
import shlex
def execute_ping(host):
    try:
        result = subprocess.run(['ping', '-c', str(1), shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)