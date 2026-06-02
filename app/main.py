from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Use subprocess.Popen without shell=True for safer execution
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode(), error.decode()

@app.get("/ping")
def ping(host: str):
    output, error = safe_ping(host)
    if error:
        return {'status': 'failed', 'error': error}
    else:
        return {'status': 'completed', 'output': output}