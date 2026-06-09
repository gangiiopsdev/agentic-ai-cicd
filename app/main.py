from fastapi import FastAPI
import subprocess

app = FastAPI()

def quote_string(s):
    return s.replace('"', '""')

@app.get("/ping")
def ping(host: str):
    if host and all(c.isalnum() or c in "-_" for c in host):
        subprocess.call(["ping", quote_string(host)])
        return {"status": "completed"}
    else:
        return {"status": "invalid_host"}