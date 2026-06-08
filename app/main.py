from fastapi import FastAPI
import subprocess
get_cmd_options = ['ping']
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    command = [get_cmd_options[0], host]
    result = subprocess.run(command, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}