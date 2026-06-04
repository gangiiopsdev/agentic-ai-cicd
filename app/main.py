from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', '-c', '1', shlex.quote(host)], universal_newlines=True, timeout=5)
        return output
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    return safe_ping(host)