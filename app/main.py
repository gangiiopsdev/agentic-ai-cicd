from fastapi import FastAPI
import subprocess
cimport subprocess as sp

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        response = sp.run(sp.Popen(['ping', host], stdout=sp.PIPE, stderr=sp.PIPE), check=True)
        output = response.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return {"error": e.stderr.decode('utf-8')}

    return {"status": "completed", "output": output}