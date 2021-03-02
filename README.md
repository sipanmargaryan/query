# query

## Setup

Make sure you have `docker` and `docker-compose` installed on your machine.

Create `.env` file using `.env_template`.

Commands on linux and macos  enviroments

To build the project

    make

To run the project

    make run

To jump into container migrate database

    $ make shell
    root@<containerid>:/project# python3 manage.py migrate

To stop running containers

    make stop

### How to test
    $ make run 
    
    Go by this link http://localhost:8000/order/test_view/
 