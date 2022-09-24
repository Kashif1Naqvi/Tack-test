Two folders for two tasks


1: backend  for core backend task
2: fullstack-test for both frontend and backend task


Both projects i add into one git repository


we disscuss firstly core backend task:

cd backend/

then activate the envoirment variable

for linux

source env/bin/active

then run the server

python3 manage.py runserver


then you to your desired browser: open url -> http://127.0.0.1:8000/

if you check daily performance open url ->  http://127.0.0.1:8000/daily_performance/


if you check filter_by_min_roi open url -> http://127.0.0.1:8000/filter_by_min_roi/


run the test 


python manage.py test app.tests.BackendTest.daily_performance
python manage.py test app.tests.BackendTest.filter_by_min_roi


deactivate the envoirment actiable by typeing 
 deactivate 

--------------------------------------------------------------------Full stack---------------------------

cd ../  #back one step 

cd fullstack-test/

there are two folders for frontend and backend

frontend on reactjs 
backend on python django django rest framework

run the backend server first then frontend server


cd backend/

active the envoirment

source env/bin/activate

run the server

python manage.py runserver


if you want to run the tests


Create only one test due to time issue

python manage.py test users.tests.RegisterViewTest.check_user_exist


deactivate the envoirment actiable by typeing 
 deactivate 




so we move to frontend 

cd ../  #back one step 


type

cd frontend/frontend-app/
then type


npm start

open this url -> http://localhost:3000
 show you login screen you login using if you have not a account please register the user and try to login again


 for register the user click register button

if you login home page show you other wise 401 unauthorized error

from frontend i learn quickly twlind css it's great i learn more about twlind css. 
one thing more due to time issue i don't learn Celry but i book mark it into my futrue learning list
i learn it on priority.


Note: 

for your understanding i add all the data into git


