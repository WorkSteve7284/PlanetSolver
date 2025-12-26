# PlanetSolver

Submission for the 2026 PATSA Region 8 HS Coding challenge.

Team `2098-903`

Team Members: `2098-068`, `2098-072`

Written in Python & C++

## Our approach

We can get a lot of points (up to 50!) for having the fastest & best algorithm. Because of that, we can't just use the first path that we come up with; we have to make the best possible algorithm for finding the best possible path.

We managed to use a little calculus to find that, to optimize score, there are exactly 3 unique speeds we must travel at. For a segment between the end and any resupply (as in, there are no resupplies between that segment and the end), that number is $\sqrt[3]{\frac{2k_l+1}{2k_f}}\approx 1.75$. For a segment with exactly one type of resupply between it and the end, that number is $\sqrt[3]{\frac{k_l+1}{2k_f}}\approx 1.63$. Finally, for a segment with resupply planets of both types between it and the end, that number is $\sqrt[3]{\frac{1}{2k_f}}\approx 1.49$.

Now that we can know the speeds a given path is traveled at, we only need to select the path. We realized that the commonly-used `A*` algorithm would probably be the best, but because the cost of a path is dependant on its future state, it wouldn't be accurate, and would just become a brute-force algorithm. Most other algorithms have this problem; since the score depends on the future state, we can't know it until the end. Then, we came to a realization: we can traverse the path backwards! The cost of a segment is symmetrical (doesn't change if going forwards or backwards), and going backwards turns those unknowable future states into very knowable past states.

The next issue with the algorithm was selecting a heuristic function. Setting it to 0 converts the `A*` algorithm into `Dijkstra's Algorithm`, which is still correct but may be slightly slower. The heuristic is just the lower bound for the score of a segment, which can be found by using the cost of a segment whose oxygen and food costs don't count. Then, the only thing left is to report the path!

We report the path data (speed & order) to the command line, as it is the fastest method we found. However, we also made a nicer-looking GUI using `TKinter`, for ease of verification. It renders planets, their resupply type (color of the planet), and hostile zones, as well as the names of all planets, and the path we used.

## Running

To run this, download the `.zip` archive from GitHub releases, unzip it, and run `main.py` using Python. Then, follow the instructions given in the command line.

> We don't have access to a machine running Linux or MacOS, so we only have a Windows version available. If you're running another OS, you will have to compile it yourself.

### CLI Options:

Add these to the end of your python command to use them.

> Your command would look like this: `python main.py map=Maps/ExampleMap.csv target=Target start=Earth`

- `nogui`: Does not render the galaxy & final path using `TKinter`.
- `map=<path>`: Skip the path selection screen. Does not check for the existence of the file, so typoes may crash the program.
- `target=<planet name>`: Set the target planet.
- `start=<planet name>`: Set the starting planet.


## Compilation Instructions

Compiling this requires Git, CMake, a C++ compiler, and a build system (E.G. Visual Studio or Ninja).

> The following instructions use Powershell

1. Clone the git repo

```shell
git clone https://github.com/WorkSteve7284/PlanetSolver.git
```

2. Update the submodules (pybind11)

```shell
cd PlanetSolver
git submodule update --init
```

3. Run CMake & compile

> `compile.bat` uses Ninja because it can generate a `compile_commants.json`, which is only nessecary for my IDE.

```shell
cd c++
cmake -B build
cmake --build build
```

4. Copy the compiled C++ file into the python directory.

```shell
copy ".\build\planetsolver.pyd" "..\python\"
```
