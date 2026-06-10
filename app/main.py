from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using check_output for better control and error handling
    args = ['ping', host]
    try:
        result = subprocess.check_output(args, stderr=subprocess.STDOUT)
        return {'result': result.decode()}
    except subprocess.CalledProcessError as e:
        return {'error': e.output.decode()}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)