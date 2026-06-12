from fastapi import FastAPI
import subprocess
global pinger_process

app = FastAPI()

@app.get("/"`
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global pinger_process
    if pinger_process is not None and pinger_process.poll() is None:
        pinger_process.terminate()
        pinger_process.wait()

    try:
        pinger_process = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        return {"error": str(e)}

    return {"status": "completed", "output": pinger_process.communicate()}
pinger_process = None