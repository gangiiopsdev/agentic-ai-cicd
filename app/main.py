from fastapi import FastAPI
import subprocess
gt
app = FastAPI()

def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    subprocess.run(args)

@app.get("/ping")
def ping_wrapper(host: str):
    return ping(host)