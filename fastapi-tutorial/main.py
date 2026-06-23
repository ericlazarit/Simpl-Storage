from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str = "None"
    is_done: bool = False



items=[]

## When routed to the home domain '/' It simply returns Hello World!
@app.get("/")
def root():
    return ("Hello World")

## This is a post route. This decides what happens when you post to the /items endpoint. If the item is an Item
## meaning, if it has the variables text and is_done defined, it creates a new Item and appends it to the items list

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items

## This is a get request route. It responds with an Item. The user needs simply to include an item_id and if the item_id
##is within the size of the list, returns the Item at that position.
@app.get('/items/{item_id}', response_model=Item)
def get_item(item_id: int) -> Item:
    if(item_id < len(items)):
        item = items[item_id]
        return item
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")

## This is a delete request route. Deletes the item at the item_ID position!!!
@app.delete('/items/{item_id}')
def delete_item(item_id: int):
    items.remove(items[item_id])
    return "Item deleted!"


##Another gret request, this one does not require an item_id. And so, if one is not provided, returns the first 10 items in the
@app.get('/items', response_model= list[Item])
def list_items(item_limit: int=10):
    return(items[0:item_limit])