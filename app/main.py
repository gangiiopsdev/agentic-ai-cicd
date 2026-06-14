from fastapi import FastAPI
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    # Use shlex.quote to safely escape the user input
    safe_host = shlex.quote(host)
    subprocess.call(['ping', '-c', '1', safe_host])

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    safe_ping(host)
    return {"status": "completed"}