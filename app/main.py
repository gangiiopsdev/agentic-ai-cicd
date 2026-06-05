from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate and sanitize host input
    try:
        args = ['ping', shlex.quote(host)]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'stdout': result.stdout, 'stderr': ''}
    except subprocess.CalledProcessError as e:
        return {'stdout': '', 'stderr': str(e.stderr)}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)