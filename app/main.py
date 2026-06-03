from fastapi import FastAPI
import subprocess
global_popen = subprocess.Popen,

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = global_popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = result.communicate()
        if result.returncode != 0:
            return {"status": "failed", "error": error.decode('utf-8')}
        return {"status": "completed", "output": output.decode('utf-8')}
    except Exception as e:
        return {"status": "failed", "error": str(e)}