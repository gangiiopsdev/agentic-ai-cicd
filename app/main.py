from fastapi import FastAPI
import shlex

def escape_host(host):
    return host.replace('\\', '\\\\').replace('\'', "'"')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    subprocess.call(shlex.split(f"ping {escaped_host}"))
    return {"status": "completed"}