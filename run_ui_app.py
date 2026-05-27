# Import the FastAPI app from the renamed file inside ui_scripts
from ui_scripts.api_services import app

# Start the application server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("run_ui_app:app", host="0.0.0.0", port=8000, reload=True)
