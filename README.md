# Opply Technical Assignment

## Binaries requirements

### Docker:
    
- Install docker and compose v2 ([docker desktop installation](https://docs.docker.com/get-docker/)).

## Installation

1. Make copy of example .env file and specify values for necessary environmental variables:
    ```bash
    cp example.env .env 
    ```

2. Build api service:
  
    ```bash
    docker compose build opply-api-service
    ```

## Usage

1. Launch api service:

    ```bash
    docker compose up opply-api-service
    ```

## Cloud Deployment
For AWS I would suggest to use following setup: ECS cluster (Fargate) + S3 + CloudFront (CDN) + RDS (Aurora)
