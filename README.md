# Django-Redis-Vue
Created a Django app using Redis database.
Integrated backend APIs with Vue.js
# Backend
Django app is located at `/django-app/django_redis`
### Installation
<p>```pip3 install python3```</p>
 <p>```pip3 install Django==3.1.7```</p>
  <p>```sudo apt install redis-server```</p>
 <p> ```pip3 APScheduler==3.7.0``` </p>
 <p> ```pip3 django-cors-headers==3.7.0```</p>
  <p>```pip install -r requirements.txt```</p>

### Running the local server

`python3 manage.py runserver --noreload`


### API Endpoints
Base URL: `http://165.22.214.254`
GET `/api/search?name=HDFC`
Body:

```
{
    "key": "HDFC",
    "SearchResults": [
        {
            "keyname": "HDFC",
            "open": "3000",
            "high": "10000",
            "low": "500",
            "close": "400"
        }
    ],
    "msg": "success"
} 
```

#Frontend 

Vue app is located at `/frontend`

###Installation
   `npm install --global vue-cli`

### Running the local server
    `npm run serve`

