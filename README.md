# Barnes-Hut-n-body-simulation
n body simulation of large celestial objects [>50k particles] using Quadtrees and Barnes-hut algorithm

*How it works-*
Barnes hut algorithm uses quadtrees to optimize n^2 calculations per frame to O(nlogn). 
This is done by approximating force calculations to center of mass of quadrants far enough from a particle rather than brute force NxN calculations.


![300x300noise](https://github.com/satmxd/Barnes-Hut-n-body-simulation/assets/122893966/c4b2dc24-e8af-4cdb-bdce-7c71c8caac2e)

[~25k particles]

Utilized algorithm is faster but at the cost of accuracy since some forces are ignored when particles are far enough.


~ More info:
https://www.cs.princeton.edu/courses/archive/fall03/cs126/assignments/barnes-hut.html
