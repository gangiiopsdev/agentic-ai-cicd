from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Add your validation logic here
    return True

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    output, error = safe_ping(host)
    if error:
        return {'status': 'failed', 'error': error}
    else:
        return {'status': 'completed', 'output': output}

def safe_ping(host):
    # Use subprocess.Popen without shell=True for safer execution
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode(), error.decode()