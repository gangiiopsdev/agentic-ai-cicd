from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    subprocess.call(args)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Secure implementation using check_output
        result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": result}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e)}