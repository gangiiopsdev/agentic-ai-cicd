from fastapi import FastAPI
import subprocess

global host
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Safe implementation using subprocess.Popen with explicit path
        result = subprocess.run(["/bin/ping", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        output = result.stdout.decode()
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}
    except Exception as e:
        return {"status": "exception", "error": str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}