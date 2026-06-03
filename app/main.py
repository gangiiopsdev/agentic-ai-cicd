from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation using subprocess.Popen instead of shell=True
    args = ['ping', host]
    result = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = result.communicate()
    return output.decode(), error.decode()
app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)