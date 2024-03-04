# Final Project for ECE-366 "Software Engineering and Large System Design"
### Cooper Union, Spring 2024
> #### Lani Wang, James Ryan, Evan Rosenfeld, Vaibhav Hariani

## Cloning the Repo
Clone the repo (with the recursive flag!) by running
```
$ git clone --recurse-submodules https://github.com/ECE-366-Final-Project/Back-End.git
```

## Build & Run  
Dependencies:  
Make sure that docker and docker-compose are installed  
[See the Docker docs for instructions!!!!!!!!!!](https://docs.docker.com/compose/install/linux/)

Build and initialize the project with <br>
```
$ docker compose up --build -d
```
Ensure that ports `8080` and `5432` are not already bound! <br>

Run the command line interface by typing

```
python3 ./commandline/cmdline.py
```

## API
Sample ping request (Default port is `8080`)        <br>
```
$ curl "localhost:<PORT>/Ping"
```

Formatting for API requests                 <br>
(localhost only if API is running locally)  <br>
```
$ curl "localhost:<PORT>/<COMMAND>?<param1>=<value>&<param2>=<value>"
```

## Database Schema
(![Schema](https://github.com/ECE-366-Final-Project/Back-End/assets/60847314/1efa2dac-ede5-491e-9d7c-46460fc67cd2))
