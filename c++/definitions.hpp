#pragma once

#include <array>
#include <cstddef>

using planet_index = int;
using precision = double;

constexpr precision cube_root(precision n) {
    precision x = 1.0;

    for (std::size_t i = 0; i < 7; i++) {
        x = (2 * x + n / (x*x)) / 3;
    }

    return x;
}

constexpr precision MAX_FOOD = 2000;
constexpr precision MAX_OXYGEN = 2000;
constexpr precision MAX_FUEL = 3000;

constexpr precision K_L = 0.3;
constexpr precision K_F = 0.15;

constexpr std::array<precision, 3> optimal_speeds = {
    cube_root((2*K_L + 1) / (2 * K_F)), // All count
    cube_root( (K_L + 1) / (2 * K_F)), // one count
    cube_root( (1) / (2 * K_F)) // None count
};