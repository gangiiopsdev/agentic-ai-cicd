from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_ping(host: str):
    try:
        output = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    result = run_ping(host)
    return {'status': 'completed', 'result': result}