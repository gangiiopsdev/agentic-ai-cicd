from fastapi import FastAPI, HTTPException
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to ensure it's a safe hostname
    if not host.replace('.', '').isalnum() or '@' in host:
        raise HTTPException(status_code=400, detail='Invalid hostname')
    result = SafePing.safe_ping(host)
    return {"status": "completed", "result": result}