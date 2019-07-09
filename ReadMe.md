# Load Testing

Now that we have a basic flask application running within docker, let's push it to the max!

## Installation

1. Run `pipenv sync` to create your virtual enviornment and install all dependencies.
1. Run `pipenv shell` to activate your virtual environment.
1. Run `locust --host=http://example.com` where example.com points to your local docker point
1. Open locust's ui at [http://localhost:8089](http://localhost:8089)

## Running a stress test

1. Input your number of users
1. Input your hatch rate (ramp rate)
1. Hit start and watch your swarm go!

## Contributions

Contributions are welcome, just open an issue or make a PR. This example will stress a docker container in my namespace.

