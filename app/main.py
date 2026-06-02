from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        args = shlex.split('ping ' + host)
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'result': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}