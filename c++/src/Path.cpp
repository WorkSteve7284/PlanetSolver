#include "Path.hpp"
#include "definitions.hpp"

Paths::Segment::Segment(planet_index start, planet_index end, precision speed) : start(start), end(end), speed(speed) {}