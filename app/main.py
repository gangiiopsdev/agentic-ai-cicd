from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "result": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "result": str(e)}