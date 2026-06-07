from fastapi import FastAPI
def get_ipython():
    return None
def run_html_magic(cell_magic_name, cell):
    return "<div style='text-align:center;'>This code cannot be executed in this environment.</div>"
app = FastAPI()
# Example endpoint to demonstrate usage
@app.get('/')
def read_root():
    return {'message': 'Hello World'}