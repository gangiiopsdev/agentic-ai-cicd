from fastapi import FastAPI
import re
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Basic validation of host
    if not re.match(r'^[a-zA-Z0-9.-]*$', host):
        return 'Invalid host'

    args = shlex.split('ping -c 1 ' + host)
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}