from fastapi import FastAPI
import subprocess
cimport os
cfrom multiprocessing import Process
c
app = FastAPI()

c@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

c@app.get("/ping")
def ping(host: str):
    process = Process(target=run_ping, args=(host,))
    process.start()
    process.join()
    return {"status": "completed"}

cdef run_ping(host: str):
    subprocess.call(["ping", host])