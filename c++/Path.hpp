#pragma once

#include "definitions.hpp"

namespace Paths {

    struct Segment {
        planet_index start, end;
        precision speed;
        Segment(planet_index, planet_index, precision);
    };
}