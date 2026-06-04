from fastapi import FastAPI
import subprocess
global host
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        # Safe implementation using subprocess.Popen
        result = subprocess.Popen(["ping", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = result.communicate()
        if error:
            return {"status": "failed", "error": error.decode()}
        else:
            return {"status": "completed", "output": output.decode()}
    except Exception as e:
        return {"status": "exception", "error": str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}