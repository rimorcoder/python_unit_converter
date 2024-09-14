from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

# Set up the Jinja2 templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Homepage"})

@app.get("/length", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("length.html", {"request": request, "message": "Length"})

@app.get("/weight", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("weight.html", {"request": request, "message": "weight"})

@app.get("/temperature", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("temperature.html", {"request": request, "message": "temperature"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)