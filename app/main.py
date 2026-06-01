from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        args = ['ping', host]
        result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {"status": "completed", "response": response}