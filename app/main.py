from fastapi import FastAPI
import subprocess
cimport = subprocess.run(
    ["ping", host],
    check=False,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = cimport.stdout.decode('utf-8') if not cimport.stderr else cimport.stderr.decode('utf-8')
    return {"status": "completed", "result": result}