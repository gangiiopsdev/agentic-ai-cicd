from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Sanitize input and use shlex for safe argument parsing
    host = host.strip().replace(' ', '_')
    command = ['ping', shlex.quote(host)]
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)