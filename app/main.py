from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    try:
        response = run_ping(host)
        return {"status": "completed", "response": response}
    except Exception as e:
        return {"error": str(e)}