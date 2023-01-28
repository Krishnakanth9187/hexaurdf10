# Moto-Roach-Simulation
In this project an adaptive walking algorithm is developed for a hexapod robot (Moto-Roach) with each leg having 3 degrees of freedom. The algorithm has the ability to adapt its walking gait ie it should vary its walking speed and change its walking gait in accordance with the roughness of the terrain. The various applications of this project include search and rescue, surveillance, terrain mapping etc.

![Moto-Roach](/Moto-Roach.jpg?raw=true "Moto-Roach")

# Install

Clone in your catkin workspace and catkin_make it:```git clone https://github.com/Krishnakanth9187/hexaurdf10.git```
# Procedure
1. 
2. To launch the simulation world:```roslaunch hexaurdf10 gazebo.launch```
3. To run gait transitions from tripod to slow tripod gait:
```rosrun hexaurdf10 hexa_walk3.py```
4. To run gait transitions from tripod to wave gait:
```rosrun hexaurdf10 hexa_walk4.py```
