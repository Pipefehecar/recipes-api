# Recipes API

This is a Django-based project named Recipes API that uses Docker for building and deploying the application, Flake8 for code quality control, and unit tests to ensure the correct functionality of the code.

## Requirements

- Docker
- Docker Compose

## Setting Up the Development Environment

1. Clone this repository to your local machine.

```bash
git clone https://github.com/username/recipes-api.git
```

2. Navigate to the project directory.

```bash
cd recipes-api
```

3. Build and start the Docker containers.

```bash
docker-compose -f docker/docker-compose.yml up --build
```

The application should now be running at `localhost:8000`.

## Testing

To run the tests, you can use the following command:

```bash
docker-compose -f docker/docker-compose.yml run app sh -c "python manage.py test && flake8"
```

This command will run the unit tests and then run Flake8 to check the code quality.

## Deployment

To deploy the application, you can use Docker. Make sure you have Docker and Docker Compose installed on your production server, then follow the same steps as for setting up the development environment.
