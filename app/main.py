from fastapi import FastAPI
import subprocess
gl = globals()
app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run without shell=True
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app.get("/ping")(ping)