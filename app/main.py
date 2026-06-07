from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode(), stderr.decode()

@app.get("/ping")
def ping(host: str):
    output, error = run_ping(host)
    if error:
        return {'status': 'error', 'message': error}
    else:
        return {'status': 'completed', 'output': output}