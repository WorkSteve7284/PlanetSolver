# PlanetSolver

Submission for the 2026 PATSA Region 8 HS Coding challenge.

Team #: 2098-903

Written in Python & C++!

## Our approach

We can get a lot of points (up to 50!) for having the fastest & best algorithm. Because of that, we can't just use the first path that we come up with; we have to make the best possible algorithm for finding the best possible path. At the time of writing this, we haven't finalized our approach, but here's our current thought process:

We have to balance correctness with speed. Because we don't have a good algorithm yet, we'll focus on speed. The two of us have fairly different experience with coding, with me (the one writing this) having decent experience in C++ & Python, and the other team member having experience in Python. Python's standard library is much more powerful for some things, while C++ is much faster than Python. Because of that, we'll use Python to first parse the CSV & convert it into a usable format, and to report the results to the judges. We'll then use C++ to actually find our answer as fast as possible. To join the two, we'll use [pybind11](https://pybind11.readthedocs.io/en/latest/).

So, now into more specifics&mdash;exactly how our approach goes. We can split the problem into several sub-problems, some of which are already solved:

1. Parse CSV into a data structure (Python)
2. Pass that to C++ (pybind11)
3. Find best possible path (C++)
    * Find all possible paths
    * Calculate best score for each path
    * Find best path
4. Find score for said path (C++)
5. Send solution back to Python (pybind11)
6. Report our solution (Python)

This approach isn't final, of course. It might change as we change our algorithm.

## Running

Running this requires Python. To run it, simply `cd` into the directory in which `main.py` is, and run `python main.py`.

### Options:

- `nogui`: Does not render the galaxy & final path
- `target=<path>`: Skip the path selection screen, and start immediately. Does not check for the existence of the file, so typoes may crash the program.


## Compilation Instructions

Compiling this requires Git, CMake, a C++20 compiler, a build system (E.G. Visual Studio or Ninja).

> This codebase uses several features from C++ 20. As of writing this, the latest versions of all major compilers (GCC, Clang, MSVC, Xcode) should support it.

> The following instructions use Powershell

1. Clone the git repo

```
git clone https://github.com/WorkSteve7284/PlanetSolver.git
```

2. Update the submodules (pybind11)

```
cd PlanetSolver
git submodule update --init
```

3. Run CMake & compile (example uses Ninja, but removing the `-G Ninja` allows CMake to select the generator itself. This shouldn't matter, I just prefer Ninja)

```
cd c++
cmake -B build -G Ninja
cmake --build build
```

4. Copy the compiled C++ file into

```
copy ".\build\planetsolver_cxx.pyd" "..\python\"
```