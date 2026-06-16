from fastapi import FastAPI
import subprocess
gethostbyname = "ping {}
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    try:
        ip_address = socket.gethostbyname(host)
        result = subprocess.call([gethostbyname.format(ip_address)], shell=False)
        return {"status": "completed", "result": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}