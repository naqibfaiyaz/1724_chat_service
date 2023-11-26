# Chat MS service

✅ Client = React frontend

✅ Krakend = API gateway

✅ auth0 = authentication microservice

✅ backend = chat microservice

client communicates with api gateway for all rest APIs. But client directly communicates with backend for socket.io.

To run the project do the follwing:

The instructions are for a windows machine, running docker desktop and git bash as terminal.

1. Run redis in container
```bash
$ docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
```

2. get your local IP address
```bash
$ ipconfig
```

3. Run chat microservice in container
```bash
$ git clone https://github.com/naqibfaiyaz/1724_chat_service
$ cd backend
$ cp .env.example .env
```
change REDIS_ENDPOINT_URL value in .env file based on your local ip address; then run the following
```bash
$ docker build --tag 'chat_service' .
$ docker run -d --name chat_service -p 5000:5000 chat_service:latest
```

4. Run auth microservice in container
```bash
$ cd ../auth_ms
$ cp .env.example .env
```
change CHAT_ENDPOINT_URL value in .env file based on your local ip address; then run the following
```bash
$ docker build --tag 'auth0' .
$ docker run -d --name auth0 -p 5005:5005 auth0:latest
```

5. Run API Gateway Krakend
```bash
$ cd ../krakend
```
We need to change the endpoints for all the APIs, based on your hosting of chat MS and auth MS. Then run the following:
```bash
$ docker build --tag 'krakend' .
$ docker run -d --name krakend -p 8080:8080 krakend:latest
```

6. Run the frontend
```bash
$ cd ../client
$ rm yarn.lock
$ yarn install
$ yarn start
```

✅ Based on the above commands, your frontend will be accessible at localhost:3000
