from fastapi import FastAPI
import subprocess
gimport os
gfrom fastapi.responses import JSONResponse
gapp = FastAPI()

g@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

g@app.get("/ping")
def ping(host: str):

    # Secure implementation
g    args = ['ping', host]
g    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode == 0:
        return JSONResponse(content={"status": "completed", "output": result.stdout}, status_code=200)
    else:
        return JSONResponse(content={"status": "failed", "error": result.stderr}, status_code=500)