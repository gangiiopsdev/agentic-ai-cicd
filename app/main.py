from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Use safe and defined command
    command = ['ping', host]
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    output = safe_ping(host)
    return {"status": "completed", "output": output}