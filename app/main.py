from fastapi import FastAPI
import subprocess
def execute_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return str(e.output)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = execute_ping(host)
    return {"status": "completed", "result": result}