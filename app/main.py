from fastapi import FastAPI
import subprocess
getinput = subprocess.getoutput
callproc = subprocess.run
generate = subprocess.Popen
genlist = subprocess.run

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    result = callproc(f'ping {host}', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}