from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it only contains allowed characters (e.g., alphanumeric and hyphen)
    if not re.match(r'^[a-zA-Z0-9-]+$', host):
        raise HTTPException(status_code=400, detail="Invalid host")
    
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}