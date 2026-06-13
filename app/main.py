from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using Popen and list instead of shell=True
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error

@app.get("/ping")
def ping(host: str):
    result, error = safe_ping(host)
    if error:
        return {'status': 'error', 'message': error.decode()}
    return {'status': 'completed', 'result': result.decode()}