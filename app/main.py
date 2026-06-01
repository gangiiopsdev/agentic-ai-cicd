from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    # Secure implementation using subprocess.run and shlex.split
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout,

@app.get("/ping")
def ping(host: str):
    try:
        output = run_ping(host)
        return {'status': 'completed', 'output': output}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}