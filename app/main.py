from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_ping(host):
    try:
        # Use shlex.quote to safely escape the host input
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)