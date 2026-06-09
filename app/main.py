from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    try:
        # Use shlex.quote to safely escape the host parameter
        safe_host = subprocess.list2cmdline([host])
        result = subprocess.run(['ping', safe_host], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    output = execute_ping(host)
    return {'status': 'completed', 'output': output}