from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    # Secure implementation
    if not host:
        return {"error": "Host parameter is required"}
    try:
        command = ['ping', '-c', '1', host]
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        return {'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'error': e.output.decode()}