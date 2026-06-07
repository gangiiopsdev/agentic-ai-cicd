from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Simple validation to prevent special characters and large inputs
        if not host.isalnum() or len(host) > 255:
            raise ValueError("Invalid hostname")
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "error", "message": str(e)}