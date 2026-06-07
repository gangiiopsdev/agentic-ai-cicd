from fastapi import FastAPI
import subprocess
global_params = {"ping": "-c 1", "host": None}
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    global_params["host"] = host
    try:
        result = subprocess.run(["ping", global_params["ping"], global_params["host"]], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}