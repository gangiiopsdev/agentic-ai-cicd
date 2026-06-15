from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    # Secure implementation
    args = ['ping', host]
    try:
        result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        return e.stderr.decode()

@app.get("/ping")
def ping(host: str):
    output = run_ping(host)
    if 'error' in output.lower():
        return {'error': output}
    else:
        return {'status': 'completed', 'output': output}