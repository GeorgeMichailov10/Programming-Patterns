# Querying a database example

import asyncio

async def simulate_db_query(id):
    objs = {
            1: 'george',
            2: 'robert',
            3: 'zlatko'
        }
    
    await asyncio.sleep(1)
    return objs[id]


async def demonstrate_async():
    id = 1

    # Goal: We want to do some stuff unrelated to the db query, query the db, print the result.
    # Make query first
    query_task = asyncio.create_task(simulate_db_query(id))

    # Simulate performing logic
    for i in range(5):
        await asyncio.sleep(0.05)

    # Make sure to now wait to get the result
    name = await query_task
    print(name)

asyncio.run(demonstrate_async())
