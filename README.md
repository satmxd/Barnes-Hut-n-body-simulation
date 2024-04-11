# Barnes-Hut-n-body-simulation
n body simulation of large celestial objects [>50k particles] using Quadtrees and Barnes-hut algorithm

*How it works-*
Barnes hut algorithm uses quadtrees to reduce the time complexity of n-body problem from  O(n^2) to O(nlogn). 
This is done by approximating force calculations to the center of mass of quadrants far enough from a particle rather than brute force NxN calculations.
As seen below, the quadtree structure is rebuilt in every frame to reduce computation.

![300x300](https://github.com/satmxd/Barnes-Hut-n-body-simulation/assets/122893966/4ad7941c-eebf-46ae-8828-8fe9a3d9d957)

~ Gallery:

[~50k particles]

![300x300noise](https://github.com/satmxd/Barnes-Hut-n-body-simulation/assets/122893966/1eda015b-3717-4d27-8632-f54b618c3374)                                
![300x300noise-slow](https://github.com/satmxd/Barnes-Hut-n-body-simulation/assets/122893966/cbcb032e-64d4-4ab4-a50e-264768a29cc2)



[~25k particles]

![300x300v2](https://github.com/satmxd/Barnes-Hut-n-body-simulation/assets/122893966/81e5e48f-4475-4acf-8da5-8dc4a1bb150b)




~ Future improvements:
OpenGL or CUDA can be used to improve the usage of GPU and increase performance by up to 10x using parallel computing/multithreads.
The utilized algorithm is faster but at the cost of accuracy since some forces are ignored when particles are far enough.
The use of Cython can be made to further increase the speed of calculations/quadtree construction.


~ More info:
https://www.cs.princeton.edu/courses/archive/fall03/cs126/assignments/barnes-hut.html
