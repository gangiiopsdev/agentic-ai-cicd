from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

def safe_ping(host: str):
    try:
        # Use shlex.quote to safely escape the host parameter
        output = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True)
        return output.stdout
    except Exception as e:
        return str(e)

def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}