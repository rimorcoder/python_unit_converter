from fastapi import FastAPI, Form, HTTPException, Query
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()
# Mount the static directory to serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up the Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Routes
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/length", response_class=HTMLResponse)
async def read_roott(request: Request, result: str = Query(""), error: str = Query("")):
    return templates.TemplateResponse("length.html", {"request": request, "result": result, "error": error})

@app.get("/weight", response_class=HTMLResponse)
async def read_weight(request: Request, result: str = Query(""), error: str = Query("")):
    return templates.TemplateResponse("weight.html", {"request": request, "result": result, "error": error})

@app.get("/temperature", response_class=HTMLResponse)
async def read_temperature(request: Request, result: str = Query(""), error: str = Query("")):
    return templates.TemplateResponse("temperature.html", {"request": request, "result": result, "error": error})

@app.post("/convert", response_class=HTMLResponse)
async def convert(request: Request, input_value: float = Form(...), convert_to: str = Form(...), convert_from: str = Form(...)):

    # temperature
    if convert_to in ["celsius", "fahrenheit", "kelvin"] or convert_from in ["celsius", "fahrenheit", "kelvin"]:
        try:    
            converted_value = convert_temperature(input_value, convert_to, convert_from)
            return RedirectResponse(url=f"/temperature?result={converted_value}", status_code=303)
        except Exception as e:
            return RedirectResponse(url=f"/temperature?error={f"Conversion failed: {e}"}", status_code=303)
    # length
    elif convert_to in ["feet", "meters", "kilometers","miles"] or convert_from in ["feet", "meters", "kilometers","miles"]:
        try:    
            converted_value = convert_length(input_value, convert_to, convert_from)
            return RedirectResponse(url=f"/length?result={converted_value}", status_code=303)
        except Exception as e:
            return RedirectResponse(url=f"/length?error={f"Conversion failed: {e}"}", status_code=303)
    # weight
    elif convert_to in ["ounce", "pound", "milligram","gram","kilogram"] or convert_from in ["ounce", "pound", "milligram","gram","kilogram"]:
        try:    
            converted_value = convert_weight(input_value, convert_to, convert_from)
            return RedirectResponse(url=f"/weight?result={converted_value}", status_code=303)
        except Exception as e:
            return RedirectResponse(url=f"/weight?error={f"Conversion failed: {e}"}", status_code=303)
    else:
        raise HTTPException(status_code=400, detail="Invalid conversion types")


# Convervsion Functions
def convert_temperature(value: float, to_unit: str, from_unit: str) -> float:
    if from_unit == to_unit:
        return value

    # Convert from the source unit to Celsius first
    if from_unit == "celsius":
        celsius_value = value
    elif from_unit == "fahrenheit":
        celsius_value = (value - 32) * 5.0 / 9.0
    elif from_unit == "kelvin":
        celsius_value = value - 273.15
    else:
        raise ValueError(f"Unsupported from_unit: {from_unit}")

    # Convert from Celsius to the target unit
    if to_unit == "celsius":
        return celsius_value
    elif to_unit == "fahrenheit":
        return celsius_value * 9.0 / 5.0 + 32
    elif to_unit == "kelvin":
        return celsius_value + 273.15
    else:
        raise ValueError(f"Unsupported to_unit: {to_unit}")

def convert_length(value: float, to_unit: str, from_unit: str) -> float:
    # Conversion factors to meters
    conversion_factors_to_meters = {
        "feet": 0.3048,
        "meters": 1.0,
        "kilometers": 1000.0,
        "miles": 1609.34
    }

    if from_unit not in conversion_factors_to_meters:
        raise ValueError(f"Unsupported from_unit: {from_unit}")
    if to_unit not in conversion_factors_to_meters:
        raise ValueError(f"Unsupported to_unit: {to_unit}")

    # Convert from the source unit to meters first
    meters_value = value * conversion_factors_to_meters[from_unit]

    # Convert from meters to the target unit
    converted_value = meters_value / conversion_factors_to_meters[to_unit]

    return converted_value

def convert_weight(value: float, from_unit: str, to_unit: str) -> float:
    conversion_factors = {
        "ounce": 1,
        "pound": 16,
        "milligram": 28349.5,
        "gram": 28.3495,
        "kilogram": 0.0283495
    }

    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Invalid unit provided")

    # Convert the value to ounces first
    value_in_ounces = value / conversion_factors[from_unit]

    # Convert from ounces to the target unit
    converted_value = value_in_ounces * conversion_factors[to_unit]

    return converted_value

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)