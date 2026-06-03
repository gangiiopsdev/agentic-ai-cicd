from fastapi import FastAPI
import subprocess
globals = {'ping': None}
app = FastAPI()
def execute_ping(host):
    args = ['ping', host]
    if globals['ping'] is None:
        globals['ping'] = subprocess.run(args, shell=False)
@app.get("/ping")
def ping(host: str):\n    # Secure implementation
    execute_ping(host)
    return {"status": "completed"}