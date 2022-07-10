from fastapi import APIRouter
from app.schemas import User, UserId


router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


list_users = []

@router.get("/")
async def index():
    return {'message': 'first application fastapi'}

@router.get("/")
async def getuser():
    return list_users

@router.post("/")
async def createuser(name: User):
    usuario = name.dict()
    list_users.append(usuario)
    return {"message": "User created with success"}

@router.get("/{user_id}")
async def finduser(user_id: int):
    for user in list_users:
        if user["id"] == user_id:
            return {"usuario": user}
    return {"message": "user not exist"}

@router.post("/getuser")
async def getuser_id(user_id: UserId):
    for user in list_users:
        if user["id"] == user_id.id:
            return {"usuario": user}
    return {"message": "user not exist"}

@router.delete("/{user_id}")
async def delete_user_id(user_id: int):
    for indx, user in enumerate(list_users):
        if user['id'] == user_id:
            list_users.pop(indx)
            return {"message": "user removed"}
    return {"message": "user not exist"}

@router.put("/{user_id}")
async def update_user(user_id: int, updateUser: User):
    for indx, user in enumerate(list_users):
        if user["id"] == user_id:
            list_users[indx]["id"] = updateUser.dict()["id"]
            list_users[indx]["name"] = updateUser.dict()["name"]
            list_users[indx]["lastname"] = updateUser.dict()["lastname"]
            list_users[indx]["address"] = updateUser.dict()["address"]
            list_users[indx]["phone"] = updateUser.dict()["phone"]
            return {"message": "user update success"}
    return {"message": "user not exist"}
