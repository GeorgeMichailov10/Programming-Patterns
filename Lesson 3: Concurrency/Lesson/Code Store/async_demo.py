# Querying database

import asyncio

async def simulate_db_query(id):
    objs = {
            1: 'george',
            2: 'robert',
            3: 'zlatko'
        }

    # Simulate delay
    await asyncio.sleep(1)
    return objs[id]

async def demonstrate_async():
    id = 1
    # Make query first async so that data is here when we need it
    query_task = asyncio.create_task(simulate_db_query(id))

    # Simulate some sort of logic
    for i in range(5):
        await asyncio.sleep(0.05)

    # Make sure to now await the query (have to make sure it exists)
    name = await query_task
    print(name)

asyncio.run(demonstrate_async())

