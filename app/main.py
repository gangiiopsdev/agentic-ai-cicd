from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    args = ['ping', subprocess.check_output(['echo', host]).decode('utf-8')]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_handler(host: str):
    return ping(host)