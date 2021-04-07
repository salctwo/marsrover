# Mars Rover task

## Description

Develop an API that moves a rover around a grid.
Your task is only provide an implementation of the `action` function inside `service.py` file.
Nothing else must be modified.

### Rules
1. You are given the initial starting point (0, 0, N) of a rover
2. 0,0 are X,Y coordinates on a grid of (10, 10)
3. N is the direction it is facing (N, S, E, W)
4. L and R allow the rover to rotate left and right around the grid
5. M allows the rover to move one point in the current direction
6. The rover receives a char array of commands e.g. RMMLM and returns the
finishing point after the moves e.g. 2:1:N
7. The rover wraps around if it reaches the end of the grid

## UnitTests
Run `python test.py`

### Usage local
Run `python main.py`

HTTP GET to see grid and Rover postition:
```
curl --request GET http://localhost:8081/ 
```

HTTP POST to send some commands to the Rover
```
curl --header "Content-Type: application/json" --request POST --data '{"command":"RMMLM"}' http://localhost:8081/
``` 

### Working example heroku
HTTP GET to see grid and Rover postition:
```
curl --request GET https://enigmatic-earth-39784.herokuapp.com/
 
```

HTTP POST to send some commands to the Rover
```
curl --header "Content-Type: application/json" --request POST --data '{"command":"RMMLM"}' https://enigmatic-earth-39784.herokuapp.com/
``` 



