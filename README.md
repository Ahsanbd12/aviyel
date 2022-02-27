# aviyel

# Requirements
1. Python v3.9.10
2. Django v4.0.2
3. Djangorestframework v3.13.1

#### Installation Guide

1. Navigate to some directory named aviyel
2. git clone https://github.com/Ahsanbd12/aviyel.git
3. source venv/bin/activate
4. pip3 install -r requirements.txt


### Postgres DB Dependencies
1. pip install psycopg2-binary
2. open postgres terminal
  a. `create DATABASE aviyel;`
  b. `create user user_name with encrypted password 'mypassword';`
  c. `grant all privileges on database sample_db to user_name;`

### Run migrations
- Navigate to aviyel directory
- Run `python3 manage.py migrate`

### Run project
- run `python3 manage.py runserver`

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
