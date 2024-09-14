# Unit Converter
 
https://roadmap.sh/projects/unit-converter

## Overview
This is a FastAPI application designed to serve both static files and dynamic content. The application uses FastAPI for handling HTTP requests, Jinja2 for templating, and Starlette for request handling. Static files are served from the static directory.

## Features
Static File Serving: The application serves static files from the static directory.
Dynamic Content: Uses Jinja2 templates to render dynamic HTML content.
Form Handling: Supports form submissions using FastAPI's Form class.
Query Parameters: Handles query parameters using FastAPI's Query class.
Exception Handling: Uses FastAPI's HTTPException for error handling.

## Installation
Clone the repository:
```
git clone <repository-url>
cd <repository-directory>
```

## Create a virtual environment:
```
python -m venv venv
source venv/bin/activate  
# On Windows use `venv\Scripts\activate`
```

## Install dependencies:
```
pip install -r requirements.txt
```

## Usage
### Run the application:
```
uvicorn app.main:app --reload
```

### Access the application: 
Open your web browser and navigate to http://127.0.0.1:8000.

## Project Structure
```
.
├── app
│   ├── main.py
│   ├── templates
│   │   └── index.html
│   └── static
│       ├── css
│       ├── js
│       └── images
├── requirements.txt
└── README.md
```

- **app/main.py**: The main entry point of the application.
- **app/templates**: Directory containing Jinja2 templates.
- **app/static**: Directory containing static files (CSS, JavaScript, images).
- **requirements.txt**: File listing the dependencies required for the project.
- **README.md**: This README file.
## Dependencies
- **FastAPI**: For building the web application.
- **Jinja2**: For templating.
- **Starlette**: For request handling.
- **Uvicorn**: For running the ASGI server.