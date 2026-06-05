from fastapi import FastAPI
import subprocess
global host_var
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    global host_var
    host_var = host

@app.on_event("startup")
def startup_event():
    try:
        subprocess.run(f"ping {host_var}", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ping failed with error: {e})"