from fastapi import FastAPI
import subprocess
global_vars = globals()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with check=True and shell=False
    try:
        subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}

# Ensure that the app variable is not accessible from outside the module
app = global_vars.pop('app')