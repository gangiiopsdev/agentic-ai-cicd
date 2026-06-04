from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Construct the ping command safely using list of arguments
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):