# Email check application
__________________________________________________________________

## How to start
__________________________________________________________________
Firstly, clone project:
```bash
git clone https://github.com/VitaliiFedin/Email_verification.git
```
To start application you need to create .env file with variables (examples in .env.sample) in folder where manage.py.Then run command
```bash
docker-compose up --build -d
```

## How to execute commands inside docker container
___________________________________________________________________
```bash
docker exec -it web-container bash
```