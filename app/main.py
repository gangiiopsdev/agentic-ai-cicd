from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/""
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get(
    "/ping",
    response_model=dict,
    responses={200: {"model": dict}}
)
def ping(host: str):
    try:
        # Use subprocess.run with shell=False for a safer approach
        result = subprocess.run(
            ["ping", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}