from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    try:
        # Use subprocess.run instead of subprocess.call and avoid shell=True for better security
        subprocess.run(['ping', host], check=True, timeout=5)
        return {"status": "completed", "result": "Success"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    except Exception as e:
        return {"status": "failed", "error": str(e)}