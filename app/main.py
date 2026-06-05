from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

decorator_options = {
    'summary': "Ping a host",
    'description': "This endpoint pings the specified host and returns the output."
}

@app.get("/ping", **decorator_options)
def ping(host: str):
    try:
        # Safe implementation using subprocess.run with shell=False and passing args as a list
        result = subprocess.run(['ping', *shlex.split(host)], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}