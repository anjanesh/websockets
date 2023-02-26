import asyncio, websockets, time

async def handler(websocket, path):

    data = await websocket.recv()
    reply = f"FETCHING {data}"
    time.sleep(1)
    await websocket.send(reply)

    if (data == 'LANDLORDS'):
        for i in range(10, 20):
            data = await websocket.recv()
            reply = f"LANDLORD : {i}"
            time.sleep(1) # Time to fetch data from dataabse
            await websocket.send(reply)
        await websocket.send("DONE")

    if (data == 'TENANTS'):
        for i in range(50, 60):
            data = await websocket.recv()
            reply = f"TENANT : {i}"
            time.sleep(1) # Time to fetch data from dataabse
            await websocket.send(reply)
        await websocket.send("DONE")

start_server = websockets.serve(handler, "localhost", 8989)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()