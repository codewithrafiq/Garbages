from fastapp import app,engine
from fastapp import models
from logging import debug
import uvicorn




if __name__ == "__main__":    
    models.Base.metadata.create_all(bind=engine)
    uvicorn.run(app='fastapp:app', host="0.0.0.0", port=8000, reload=True, debug=True)
