from fastapi import FastAPI
import subprocess
global_vars = globals()
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if host not in global_vars:
        return {"error": "Invalid input"}
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True)
        return {"status": "completed", "output": output.stdout}
    except Exception as e:
        return {"error": str(e)}