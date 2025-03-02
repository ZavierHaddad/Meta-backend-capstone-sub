Check passowrd for MySQL database 

"http://127.0.0.1:8000/restaurant/index/" is my example of returning HTML

ENDPOINTS TO CHECK, PLEASE:
http://127.0.0.1:8000/restaurant/index/
http://127.0.0.1:8000/restaurant/menu/
http://127.0.0.1:8000/restaurant/user/
http://127.0.0.1:8000/restaurant/booking/

once model entries made you can also test detail views eg:
http://127.0.0.1:8000/restaurant/booking/1/
http://127.0.0.1:8000/restaurant/user/2/
http://127.0.0.1:8000/restaurant/menu/5/

etc...

For AUTH:
http://127.0.0.1:8000/auth/token/login/
Make users in admin panel then test getting token with exaple body POST message below:

{
	"username":"User1",
	"password":"Pa$$1234"
}
You should recieve token

http://127.0.0.1:8000/auth/token/logout/
Using recieved bearer token test logout with above endpoint - you should recieve 204 sucess message and token will be invlaid after 
