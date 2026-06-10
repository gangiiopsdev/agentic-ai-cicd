from fastapi import FastAPI
import subprocess
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        result = {
            "status": "completed",
            "output": output.stdout
        }
        return jsonable_encoder(result)
    except subprocess.CalledProcessError as e:
        return jsonable_encoder({
            "status": "failed",
            "error": str(e)
        })