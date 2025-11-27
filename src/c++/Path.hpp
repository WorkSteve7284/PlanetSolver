#pragma once

#include <cstddef>

#include "Resources.hpp"

/* Store paths between planets */

struct IncompletePathSegment {
    std::size_t start, end; // Index of planet (Name obtained from map)
    double min_speed, max_speed;

    IncompletePathSegment(std::size_t new_start, std::size_t new_end, double min, double max) : start(new_start), end(new_end), min_speed(min), max_speed(max) {}
};

struct PathSegment {
    std::size_t start, end;
    double speed;
};