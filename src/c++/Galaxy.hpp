#pragma once

#include <string>
#include <map>
#include <vector>

#include "Vector.hpp"

/* Create a data type for the galaxy map */

enum class ResupplyType {
    NONE,
    FOOD,
    OXYGEN
};

struct Planet {
    std::string name;
    std::size_t index;
    Vector2 position;
    ResupplyType resupply = ResupplyType::NONE;
    double hostile_radius = 0;
    bool is_hostile = false;

    // Constructors
    Planet() = default;

    Planet(const std::string& planet_name, const Vector2& pos, ResupplyType resupply_type, double radius)
    : name(planet_name), position(pos), resupply(resupply_type), hostile_radius(radius), is_hostile(hostile_radius != 0) {}

    Planet(const std::string& planet_name, const Vector2& pos, ResupplyType resupply_type, double radius, bool hostile)
    : name(planet_name), position(pos), resupply(resupply_type), hostile_radius(radius), is_hostile(hostile) {}
};

struct GalaxyMap {

    std::map<std::size_t, std::string> index_to_name;
    std::map<std::string, std::size_t> name_to_index;

    std::vector<Planet> planets;

    GalaxyMap() = default; // No constructor

    void add_planet(const Planet& planet) {
        planets.push_back(planet);

        index_to_name[planets.size() - 1] = planet.name;
        name_to_index[planet.name] = planets.size() - 1;
    }
};