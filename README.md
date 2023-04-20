# NASA APOD API

The purpose of this project is to consume NASA's Astronomy Picture of the Day API.

The data requested from NASA's Astronomy Picture of the Day API is saved in a MongoDB collection.

This project is using the following technologies (see versions in requirements.txt):
- python
- requests
- python-decouple
- mongo-db
- mongoengine


For more details go to documentation.md.

# To-do
- [x] Check if response data is already in the database. Do not add data to the database if duplicated.
- [ ] Add tests.