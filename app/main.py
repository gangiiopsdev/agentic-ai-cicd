from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        if host.strip() and all(c.isalnum() or c in ['.', '-'] for c in host):
            subprocess.run(['ping', host], check=True, shell=False)
            return {"status": "completed"}
        else:
            return {"error": "Invalid hostname"}
    except Exception as e:
        return {"error": str(e)}