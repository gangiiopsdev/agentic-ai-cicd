from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    if not host.isdigit():
        raise ValueError("Invalid host")
    return host

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    validated_host = validate_host(host)
    command = ["ping", shlex.quote(validated_host)]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        return {"error": error.decode()}
    return {"message": output.decode()}