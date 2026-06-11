from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host == 'localhost' or host.startswith('127.0.0.'):  # Example validation, adjust as needed
        try:
            subprocess.run(['ping', host], check=True, shell=False)
        except subprocess.CalledProcessError as e:
            return {"error": str(e)}
    else:
        return {"error": "Invalid host"}

    return {"status": "completed"}