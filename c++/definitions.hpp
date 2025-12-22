#pragma once

#include <array>
#include <cstddef>
#include <cmath>

using planet_index = int;
using precision = double;

constexpr precision cube_root(precision n) {
    precision x = 1.0;

    for (std::size_t i = 0; i < 10; i++) {
        x = (2 * x + n / (x*x)) / 3;
    }

    return x;
}

constexpr precision MAX_FOOD = 2000;
constexpr precision MAX_OXYGEN = 2000;
constexpr precision MAX_FUEL = 3000;

constexpr precision K_L = 0.3;
constexpr precision K_F = 0.15;

const std::array<precision, 3> optimal_speeds = {
    std::cbrt((2*K_L + 1) / (2 * K_F)), // All count
    std::cbrt( (K_L + 1) / (2 * K_F)), // one count
    std::cbrt( (1) / (2 * K_F)) // None count
};