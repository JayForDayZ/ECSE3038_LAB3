from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import pydantic.json
from bson import ObjectId
import motor.motor_asyncio
import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://ecse3038-lab3-tester.netlify.app/",
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    
)

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://Delco4:Database2023@ecsce3038.cx2jmyy.mongodb.net/?retryWrites=true&w=majority")
db = client.monitors

pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str

@app.get("/profile")
async def retrieve_user_profile():
    profile = await db["profile"].find().to_list(800)
    if len(profile) < 1:
        return {}
    return profile[0]

@app.post("/profile", status_code=201)
async def create_user_profile(request: Request):
    user_profile = await request.json()
    user_profile["last_updated"] = datetime.datetime.now()

    new_profile = await db["profile"].insert_one(user_profile)
    created_profile = await db["profile"].find_one({"_id": new_profile.inserted_id})

    return created_profile

@app.post("/data", status_code=201)
async def create_tanks_data(request: Request):
    tank_data = await request.json()

    new_tank = await db["tank"].insert_one(tank_data)
    created_tank = await db["tank"].find_one({"_id": new_tank.inserted_id})

    return created_tank

@app.get("/data")
async def retrieve_tanks():
    tanks = await db["tank"].find().to_list(999)
    return tanks

    

@app.patch("/data/{id}")
async def do_update(id:str, request: Request):
    updated= await request.json()
    updated_tank = await db["tank"].update_one({"_id":ObjectId(id)}, {'$set': updated})
    
    if updated_tank.modified_count == 1:
         if (
                current_tank := await db["tank"].find_one({"_id": id})
            ) is not None:
                return current_tank   
    else:
         raise HTTPException(status_code=404, detail="Item was not found")

@app.delete("/data/{id}", status_code=204)
async def delete_tank(id: str):
    result = await db["tank"].delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item was not found")