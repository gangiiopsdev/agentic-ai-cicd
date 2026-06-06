from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get"