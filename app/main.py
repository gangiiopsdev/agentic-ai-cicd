from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use shlex.quote to safely escape the host parameter
        command = ['ping', shlex.quote(host)]
        output = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return output.stdout
    except Exception as e:
        return str(e)

@app.get('/ping/{host}')
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}