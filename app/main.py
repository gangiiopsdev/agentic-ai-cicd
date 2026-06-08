from fastapi import FastAPI
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}

def safe_ping(host: str):
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, check=True)