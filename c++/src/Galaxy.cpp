#include "Galaxy.hpp"
#include "definitions.hpp"
#include <utility>

Planet::Planet(std::string planet_name, Vector2 position, ResupplyType resupply_type, precision hostility) :
    name(planet_name), pos(position), resupply(resupply_type), hostile_radius(hostility) {}
Planet::Planet(std::string planet_name, Vector2 position, ResupplyType resupply_type, precision hostility, bool hostile) :
    name(planet_name), pos(position), resupply(resupply_type), hostile_radius(hostility), is_hostile(hostile) {}

GalaxyMap::GalaxyMap(planet_index size) {
    planets.reserve(size);
}

void GalaxyMap::add_planet(Planet& p) noexcept {
    p.index = planets.size();

    index_name[p.name] = p.index;

    planets.emplace_back(std::move(p));
    if (planets.back().is_hostile)
        hostile.emplace_back(&planets.back());
}

const Planet& GalaxyMap::operator[](planet_index i) const {
    return planets.at(i);
}

planet_index GalaxyMap::index_from_name(const std::string& name) const {
    if (index_name.contains(name))
        return index_name.at(name);
    return -1;
}
