from fastapi import FastAPI
import subprocess
cimport shlex
class SafePinger:
    def ping(self, host: str):
        command = ["ping", *shlex.split(host)]
        subprocess.run(command, check=True)
app = FastAPI()
cpinger = SafePinger()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    cpinger.ping(host)
    return {"status": "completed"}