from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ⬇️ WICHTIG: dieser Import bindet die Customers-Routen ein
from .routers import customers

app = FastAPI(title="CRUD Backend", version="0.1.0")

# CORS fürs lokale Frontend (später enger stellen)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ⬇️ WICHTIG: Router registrieren
app.include_router(customers.router)

@app.get("/health")
def health():
    return {"status": "ok"}
