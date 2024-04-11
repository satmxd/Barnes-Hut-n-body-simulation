# Barnes-Hut-n-body-simulation
n body simulation of large celestial objects [>50k particles] using Quadtrees and Barnes-hut algorithm

*How it works-*
Barnes hut algorithm uses quadtrees to optimize n^2 calculations per frame to O(nlogn). 
This is done by approximating force calculations to center of mass of quadrants far enough from a particle rather than brute force NxN calculations.


![300x300noise](https://github.com/satmxd/Barnes-Hut-n-body-simulation/assets/122893966/1eda015b-3717-4d27-8632-f54b618c3374)


![300x300noise](https://github.com/satmxd/Barnes-Hut-n-body-simulation/assets/122893966/69106b9e-7ba2-4c39-98a9-a4e9f47b86f9)

[~50k particles]

Utilized algorithm is faster but at the cost of accuracy since some forces are ignored when particles are far enough.


~ More info:
https://www.cs.princeton.edu/courses/archive/fall03/cs126/assignments/barnes-hut.html
