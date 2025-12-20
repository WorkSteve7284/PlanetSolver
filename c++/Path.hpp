#pragma once

#include "definitions.hpp"

namespace Paths {

    enum class SegmentType : unsigned char {
        UNKNOWN = 0,
        ALL, // All resources count (speed ~= 1.7)
        ONE, // One of food or oxygen count (speed ~= 1.6)
        NONE // Only time & fuel count (speed ~= 1.4)
    };

    struct Segment {
        planet_index start, end;
        precision speed;
        Segment(planet_index, planet_index, precision);
    };
}