# Barnes-Hut-n-body-simulation
n body simulation of large celestial objects [>50k particles] using Quadtrees and Barnes-hut algorithm implemented in Python

*How it works-*
Barnes hut algorithm uses quadtrees to reduce the time complexity of n-body problem from  O(n^2) to O(n*log(n)). 
This is done by approximating force calculations to the center of mass of quadrants far enough from a particle rather than brute force NxN calculations.
As seen below, the quadtree structure is rebuilt in every frame to reduce computation.

The Barnes-Hut approximation involves three steps:
1. Construct the spatial index (e.g., quadtree)
2. Calculate centers of mass
3. Estimate forces

![300x300](https://github.com/satmxd/Barnes-Hut-n-body-simulation/assets/122893966/4ad7941c-eebf-46ae-8828-8fe9a3d9d957)

COM for every quadrant is calculated and the ratio width / distance is taken as a measure for threshold (theta), if it is > theta, we treat the quadtree cell as a source of long-range forces and use its center of mass.

![screenshot5](https://github.com/satmxd/Barnes-Hut-n-body-simulation/assets/122893966/214f7499-fdef-4ed7-b950-cd65a8985097)


~ Gallery:

[~50k particles]
Simulation time: ~ 1hr

![300x300noise](https://github.com/satmxd/Barnes-Hut-n-body-simulation/assets/122893966/1eda015b-3717-4d27-8632-f54b618c3374)    ![300x300](https://github.com/satmxd/Barnes-Hut-n-body-simulation/assets/122893966/0d82ecc6-cd18-415d-bdf6-8fb36a6fb887)    ![300x300noise-slow](https://github.com/satmxd/Barnes-Hut-n-body-simulation/assets/122893966/cbcb032e-64d4-4ab4-a50e-264768a29cc2)



[~25k particles]

Simulation time: ~0.5 hr

![300x300](https://github.com/satmxd/Barnes-Hut-n-body-simulation/assets/122893966/9cfc24c2-102f-46d1-8a3a-2cb70c218309)     ![300x300](https://github.com/satmxd/Barnes-Hut-n-body-simulation/assets/122893966/04dd04d6-3b73-4bbe-ab8d-8d3e634251a6)     ![300x300long](https://github.com/user-attachments/assets/d816c302-f37a-48e5-925b-0f8db95a324b)



[Stills]

<img width="300" height="300" alt="comb" src="https://github.com/user-attachments/assets/5fc78602-0be4-4e16-8381-221bf77b3606" />     <img width="315" height="315" alt="gausscoltilemap" src="https://github.com/user-attachments/assets/dd04ad93-f8f4-431b-b8df-a45c4ae0cfdc" />    <img width = "310" height = "310" alt="doublecol" src="https://github.com/user-attachments/assets/1d0a55a3-03c5-4b4a-833d-77d8c3127666"/>





~ Future improvements:
* Biggest bottleneck is the programming language, switching to c/rust can improve performance by tenfold.

* OpenGL or CUDA can be used to increase the usage of GPU and improve performance by up to 10x using parallel computing/multithreading.
  
* The utilized algorithm is faster but at the cost of accuracy since some forces are ignored when particles are far enough.
  
* Cython can be used to further increase the speed of calculations/quadtree construction.
  
* Particle collision can be added to increase accuracy of simulation


~ More info:
https://www.cs.princeton.edu/courses/archive/fall03/cs126/assignments/barnes-hut.html
