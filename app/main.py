from fastapi import FastAPI
import subprocess
cimport = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = cimport.communicate()
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": result.stdout}