from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    try:
        command = ['ping', host]
        output = subprocess.check_output(command, universal_newlines=True)
        return output
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    result = safe_ping(shlex.quote(host))
    return {'status': 'completed', 'result': result}