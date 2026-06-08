from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    # Validate and sanitize the input host
    if not host.isalnum():
        raise ValueError('Invalid host name')
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode(), stderr.decode()

@app.get("/ping")
def ping(host: str):
    try:
        output, error = run_ping(host)
        if error:
            return {'status': 'error', 'message': error}
        else:
            return {'status': 'completed', 'output': output}
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}