from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Secure implementation using subprocess.Popen
        result = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = result.communicate()
        if result.returncode != 0:
            raise Exception(f"Ping failed with error: {error.decode('utf-8')}")
        return {"status": "completed", "output": output.decode('utf-8')}
    except Exception as e:
        return {"status": "failed", "error": str(e)}