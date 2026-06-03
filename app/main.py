from fastapi import FastAPI
import subprocess
global host_list 
host_list = ['127.0.0.1', '8.8.8.8']
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if host in host_list:
        try:
            output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return {"status": "completed", "output": output.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "error", "output": e.stderr}
    else:
        return {"status": "error", "output": f'Host {host} not allowed'}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}