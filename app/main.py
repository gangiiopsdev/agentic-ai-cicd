from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use shlex.quote to safely handle the host parameter
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, str(e)

@app.get("/ping")
def ping(host: str):
    success, output = safe_ping(host)
    if not success:
        return {'status': 'failed', 'error': output}
    else:
        return {'status': 'completed', 'output': output}