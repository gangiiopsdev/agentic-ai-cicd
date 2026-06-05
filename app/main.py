from fastapi import FastAPI
import subprocess
def run_ping(host):
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return result.stdout
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        response = run_ping(host)
        return {"status": "completed", "response": response}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}