from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Using subprocess.Popen for safe execution without shell=True
    cmd = ['ping', host]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode(), error.decode()

@app.get("/ping")
def ping(host: str):
    try:
        result, err = safe_ping(host)
        if err:
            raise Exception(err)
        return {"status": "completed", "output": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}