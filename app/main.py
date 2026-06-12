from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input
    safe_host = subprocess.list2cmdline([host])
    try:
        output = subprocess.check_output(['ping', safe_host], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}