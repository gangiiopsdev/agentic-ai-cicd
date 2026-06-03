from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and check=True
delimiter = ' '.join(['ping', host])
subprocess.run(delimiter, check=True, shell=False)

@app.get("/ping")
def get_ping(host: str):
    return ping(host)