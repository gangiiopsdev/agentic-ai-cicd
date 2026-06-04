from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    # Safe implementation using subprocess.Popen
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode('utf-8'), error.decode('utf-8')

@app.get("/ping")
def ping(host: str):
    result, err = run_ping(host)
    if err:
        return {'status': 'error', 'message': err}
    else:
        return {'status': 'completed', 'result': result}