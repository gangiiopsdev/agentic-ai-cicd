from fastapi import FastAPI
import subprocess
class PingInput(BaseModel):
    host: str

app = FastAPI()

@app.get("/ping")
def ping(input: PingInput):
    # Secure implementation
    subprocess.call(["ping", input.host], shell=False)

    return {"status": "completed"}