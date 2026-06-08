from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.isnumeric():
        try:
            output = subprocess.run(['ping', host], shell=False, capture_output=True, text=True, timeout=5)
            return {"status": "completed", "output": output.stdout}
        except Exception as e:
            return {"status": "failed", "error": str(e)}
    else:
        return {"status": "invalid_host"}