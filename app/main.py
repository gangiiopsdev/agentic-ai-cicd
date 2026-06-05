from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        args = ['ping', *shlex.split(host)]
        response = subprocess.run(args, capture_output=True, text=True, check=True)
        return response.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    result = safe_ping(shlex.quote(host))  # Use shlex.quote to sanitize input
    return {'status': 'completed', 'result': result}