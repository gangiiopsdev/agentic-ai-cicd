from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    try:
        # Use shlex.quote to escape any special characters in the host input
        result = subprocess.run(['ping', shlex.quote(host)], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def safe_ping_no_shell(host):
    try:
        # Use shell=False and pass the arguments as a list to avoid shell injection
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True, shell=False)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    response = safe_ping_no_shell(shlex.quote(host))
    return {"status": "completed", "response": response}