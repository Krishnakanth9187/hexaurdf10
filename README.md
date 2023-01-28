# Moto-Roach
In this project an adaptive walking algorithm is developed for a hexapod robot (Moto-Roach) with each leg having 3 degrees of freedom. The algorithm has the ability to adapt its walking gait ie it should vary its walking speed and change its walking gait in accordance with the roughness of the terrain. The various applications of this project include search and rescue, surveillance, terrain mapping etc.
Inline-style: 
![alt text](https://github.com/Krishnakanth9187/hexaurdf10/commit/9ec349510f36ac5e99670b9269d6c2de8f84b2fe)
# Procedure
1. To launch the simulation world:```roslaunch hexaurdf10 gazebo.launch```
2. To run gait transitions from tripod to slow tripod gait:
```rosrun hexaurdf10 hexa_walk3.py```
3. To run gait transitions from tripod to wave gait:
```rosrun hexaurdf10 hexa_walk4.py```
