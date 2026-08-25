from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base,engine
from .routers import posts,users,auth,vote


# Base.metadata.create_all(bind=engine)

origins=["https://www.youtube.com/"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
        
@app.get("/")
def root():
    return "appp withhh faaassst aaapppiiii"

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)



