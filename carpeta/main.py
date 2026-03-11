from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from security import get_current_user


from database import SessionLocal, engine, Base
import models, schemas
from auth import hash_password, verify_password, create_access_token

app = FastAPI()

Base.metadata.create_all(bind=engine)



# DEPENDENCIA BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 🟦 REGISTRO
@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Usuario ya existe"
        )

    hashed = hash_password(user.password)

    new_user = models.User(
        email=user.email,
        password=hashed
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "Usuario registrado correctamente"}

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    db_user = db.query(models.User).filter(
        models.User.email == form_data.username
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Bearer"}
        )

    if not verify_password(form_data.password, db_user.password):
        raise HTTPException(
            status_code=401,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Bearer"}
        )

    token = create_access_token(
        data={"sub": db_user.email}
    )

    return {"access_token": token, "token_type": "bearer"}
    
@app.get("/protected")
def protected_route(
    current_user: str = Depends(get_current_user)
):
    return {
        "message": f"Bienvenido {current_user}"
    }
