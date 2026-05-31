from fastapi import FastAPI
def ping(host: str):
    # Secure implementation
    subprocess.call(["ping", host], shell=False)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(["ping", host], shell=False)
    return {"status": "completed"}