from fastapi import FastAPI, HTTPException
import subprocess
import re
class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Use regular expression to validate the host parameter
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid hostname')
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        result = SafePing.safe_ping(host)
        return {"status": "completed", "result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))