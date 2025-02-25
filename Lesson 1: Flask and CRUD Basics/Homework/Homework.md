You are going to build a web app similar to what we built. You are going to build a calculator CRUD
app where the user can post numbers to one route and then they can request a calculation for all of the numbers that have been stored and to get the result.

Expectations:
You have routes that do the following:
- Create a set of numbers to perform operations on in the database
- Add a number to a set of numbers
- Remove a number from a set of numbers
- Get a specific set of numbers
- Delete a set of numbers
- Get the result of operations performed on the numbers

Example: 
Post(2,3,4,5)
Get('+', '-', '*')


You may assume all calculations are done left to right and don't follow order of operations for simplicity.

Enforce that number of numbers == number of operations + 1

(HINT): The numbers should be stored in the database between route calls (so how should you set this up to be able to retrieve them? What kind of input should the routes be expecting? What should you be returning?)

You may use ChatGPT for simple syntax purposes, but the logic itself should be all yours. If you forget how to initialize the db with Pymongo or how to read in a string to a json through the method header, that's totally ok. Using it to write the operations handlind is not.
