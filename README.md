Introduction:

You will test a service that navigates a imaginary robotic hoover (much like a Roomba) through an equally imaginary room based on:

* Room dimensions as X and Y coordinates, identifying the top right corner of the room rectangle. This room is divided up in a grid based on these dimensions; a room that has dimensions X: 5 and Y: 5 has 5 columns and 5 rows, so 25 possible hoover positions. The bottom left corner is the point of origin for our coordinate system, so as the room contains all coordinates its bottom left corner is defined by X: 0 and Y: 0.
  
* Locations of patches of dirt, also defined by X and Y coordinates identifying the bottom left corner of those grid positions.
  
* An initial hoover position (X and Y coordinates like patches of dirt)
  
* Driving instructions (as cardinal directions where e.g. N and E mean "go north" and "go
east" respectively)

The room will be rectangular, has no obstacles (except the room walls), no doors and all locations in the room will be clean (hoovering has no effect) except for the locations of the patches of dirt presented in the program input.
Placing the hoover on a patch of dirt ("hoovering") removes the patch of dirt so that patch is then clean for the remainder of the program run. The hoover is always on - there is no need to enable it.
Driving into a wall has no effect (the robot skids in place).

Deliverable:

Test cases to verify the service for the following scenarios

* Service is up and running
  
* Input directions provided in the service are valid i.e; N, S, E, W
  
* Navigation of the Robot Vacuum is according to the direction instructions
  
* Validation of the number of patches cleaned by the Vacuum

System Requirements:

* Python3
* Pytest-bdd

  
 How to run the test:
 
 From the terminal in the Code Editor (IntelliJ in this case), use the below command to run the features
 
 python3 -m pytest -v tests/testcases/RobotVacuumTest.py
