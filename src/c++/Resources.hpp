#pragma once

struct Resources {
    double food, oxygen, fuel;

    Resources() = default;
    Resources(double new_food, double new_o2, double new_fuel) : food(new_food), oxygen(new_o2), fuel(new_fuel) {}
};