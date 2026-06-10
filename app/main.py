from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    # Safe implementation
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        return {"error": e.output}, 400

    return {"status": "completed", "output": output}