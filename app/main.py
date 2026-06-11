from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def sanitize_input(input_string):
    return input_string.strip().replace('\n', '').replace('\t', '')

@app.get("/ping")
def ping(host: str):