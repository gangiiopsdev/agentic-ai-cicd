from fastapi import FastAPI
import subprocess
import shlex
from fastapi.responses import JSONResponse

class PingException(Exception):
    pass

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        args = ['ping', host]
        process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        if process.returncode != 0:
            raise PingException(str(error))
        return JSONResponse(content={"status": "completed", "output": str(output)}, status_code=200)
    except PingException as e:
        return JSONResponse(content={"status": "error", "message": str(e)}, status_code=500)