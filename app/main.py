from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Secure implementation using Popen
        result = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = result.communicate()
        return {"status": "completed", "output": output.decode('utf-8'), "error": error.decode('utf-8')}
    except Exception as e:
        return {"status": "failed", "message": str(e)}