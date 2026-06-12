from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Use shlex to safely quote the host input
        command = ['ping', shlex.quote(host)]
        result = subprocess.run(command, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return str(e)