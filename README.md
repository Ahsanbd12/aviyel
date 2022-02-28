# aviyel

# Requirements
1. Python v3.9.10
2. Django v4.0.2
3. Djangorestframework v3.13.1

#### Installation Guide
1. git clone https://github.com/Ahsanbd12/aviyel.git
2. Navigate to same directory named aviyel
3. virtualenv venv
4. source venv/bin/activate
5. pip3 install -r requirements.txt


### Postgres DB Dependencies
1. Make sure you have postgres installed.
2. Open postgres terminal.
  - `create DATABASE aviyel;`
  - `create user user_name with encrypted password 'mypassword';`
  - `grant all privileges on database sample_db to user_name;`

### Set enviorment variables
Create `.env` in root directory 
1. `DATABASE_NAME=XYZ`
2. `USER=XYZ`
3. `PASSWORD=password`
4. `HOST=localhost`
5. `PORT=5432`

### Run migrations
- Run `python3 manage.py migrate`

### Run project
- Run `python3 manage.py runserver`

### Testing
- You can use Postman or any other tool to test the API endpoints

### Project URLs 
1. List all users: GET localhost:8000/api/users 
2. Cretae User: POST localhost:8000/api/users `{ "email": "example@example.com", "username": "XYZ", "password": "abcd1234" }`
3. List all conferences: GET localhost:8000/api/conferences
4. Show a specific conference: GET localhost:8000/api/conferences/<:id>
5. List a conference all talks: GET localhost:8000/api/conferences/<:id>/talks
6. Create a conference talks: POST localhost:8000/api/conferences/<:id>/talks 
    `{ "title": "XYZ", "description": "XYZ", "duration": "01:30", "schedule_date": "2022-02-02" }`
8. Show a specific conference specific talk GET localhost:8000/api/conferences/<:id>/talks/<:id>
9. Add a user in specific talks PATCH localhost:8000/api/conferences/<:id>/talks/<:id> `{ users: [user_id, user_id] }`
