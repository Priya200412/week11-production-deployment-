# Week 11 Production Deployment

## Run Development

docker-compose -f docker/docker-compose.yml up --build

## Run Production

docker-compose -f docker/docker-compose.prod.yml up -d

## Run Migrations

flask db init
flask db migrate
flask db upgrade
