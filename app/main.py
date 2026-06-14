from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not host or len(host) > 100:
        raise ValueError('Invalid host name')
    try:
        # Use shlex.quote to safely handle the command argument
        response = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True)
        return response.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'result': safe_ping(host)}