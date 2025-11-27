#pragma once

#include <algorithm>
#include <cmath>
#include <cstddef>
#include <vector>

#include "Galaxy.hpp"
#include "Path.hpp"
#include "Resources.hpp"
#include "Vector.hpp"

inline const double K_F = 0.3;
inline const double K_L = 0.15;

inline const double MAX_FOOD = 2000;
inline const double MAX_OXYGEN = 2000;
inline const double MAX_FUEL = 3000;

inline double calculate_max_speed(const Resources& resources, double dist) {
    // Calculate the max speed possible given resources
    // Speed is capped by fuel cost
    /*
    fuel cost = K_F * distance * speed^2
    fuel cost < fuel total
    K_F * distance * speed^2 < fuel total
    fuel total / (distance * K_F) > speed^2
    sqrt(fuel total / (distance * K_F)) > speed
    */

    return std::sqrt(resources.fuel / (dist * K_F));
}

inline double calculate_min_speed(const Resources& resources, double dist) {
    // Calculate the min speed possible given resources
    // Speed is required by food & oxygen
    /*
    (food & o2 are interchangeable)
    food cost = K_L * distance / speed
    food cost < food total
    food total > K_L * distance / speed
    food total * speed > K_L * distance
    speed > K_L * distance / food total
    (then pick the higher number from food & o2)
    */

    return std::max(dist * K_L / resources.food, dist * K_L / resources.oxygen);
}

inline double calculate_food_cost(double dist, double speed) {
    return K_L * dist / speed;
}
inline double calculate_fuel_cost(double dist, double speed) {
    return K_F * dist * speed * speed;
}

enum class ShipStatus {
    // Represent the status of a ship's travel
    SUCCESS,
    FAIL_RESOURCES,
    FAIL_HOSTILE
};

/* Implement the ship to go between planets */
struct Ship {
    const GalaxyMap& map;
    Resources resources;
    std::size_t current_position = 0;

    std::vector<IncompletePathSegment> history;

    Ship(const GalaxyMap& world_map) : map(world_map) {
        resources.food = MAX_FOOD;
        resources.oxygen = MAX_OXYGEN;
        resources.fuel = MAX_FUEL;
    }
    Ship(const GalaxyMap& world_map, size_t start_planet) : map(world_map), current_position(start_planet) {
        resources.food = MAX_FOOD;
        resources.oxygen = MAX_OXYGEN;
        resources.fuel = MAX_FUEL;
    }

    ShipStatus try_to_planet(size_t target) {
        if (target == current_position)
            return ShipStatus::SUCCESS;

        // Check if it goes through a hostile zone
        const Vector2 A = map.planets[current_position].position;
        const Vector2 B = map.planets[target].position;
        const Vector2 vec = A - B;

        for(const Planet& planet : map.planets) {
            if(!planet.is_hostile)
                continue;

            const double r2 = planet.hostile_radius * planet.hostile_radius;
            const Vector2 C = planet.position;

            if((B - C).sqr_magnitude() <= r2)
                return ShipStatus::FAIL_HOSTILE;

            // check if the segment intersects with the line

            const double t = std::clamp(Vector2::dot(C - A, B - A) / vec.sqr_magnitude(), 0.0, 1.0);

            if (((A + t * vec) - C).sqr_magnitude() <= r2)
                return ShipStatus::FAIL_HOSTILE;
        }

        // Check the costs
        double dist = vec.magnitude();

        double max_speed = calculate_max_speed(resources, dist);
        double min_speed = calculate_min_speed(resources, dist);

        if (max_speed < min_speed)
            return ShipStatus::FAIL_RESOURCES;

        // Subtract the costs
        resources.food -= calculate_food_cost(dist, max_speed);
        resources.oxygen -= calculate_food_cost(dist, max_speed);
        resources.fuel -= calculate_food_cost(dist, min_speed);

        history.push_back(IncompletePathSegment(current_position, target, min_speed, max_speed));
        current_position = target;

        return ShipStatus::SUCCESS;
    }
};