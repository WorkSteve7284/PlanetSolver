#pragma once

#include "Vector.hpp"
#include "definitions.hpp"
#include <string>
#include <vector>
#include <unordered_map>

enum class ResupplyType : unsigned char {
    NONE = 0,
    OXYGEN,
    FOOD
};

struct Planet {
    std::string name;

    Vector2 pos;

    planet_index index = 0;

    ResupplyType resupply;

    bool is_hostile;
    precision hostile_radius;

    Planet(std::string, Vector2, ResupplyType, precision);
    Planet(std::string, Vector2, ResupplyType, precision, bool);
};

struct GalaxyMap {

    std::vector<Planet> planets;
    std::vector<Planet*> hostile;

    GalaxyMap(planet_index);

    const Planet& operator[](planet_index) const;

    planet_index index_from_name(const std::string&) const;

    void add_planet(Planet&) noexcept;

private:
    std::unordered_map<std::string, planet_index> index_name;
};