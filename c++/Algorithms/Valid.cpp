#include "Valid.hpp"
#include "Galaxy.hpp"
#include <vector>

Algorithms::Graph::Graph(const GalaxyMap& map) {
    // Finds possible neighbors for planets

    possible_graph.resize(map.planets.size());

    for (planet_index i = 0; i < map.planets.size(); i++) {

        // Ensure planet isn't hostile
        if (map.planets[i].is_hostile)
            continue;

        const Vector2& A = map.planets[i].pos;

        for (planet_index j = i+1; j < map.planets.size(); j++) {

            // Also ensure planet isn't hostile
            if (map.planets[j].is_hostile)
                continue;

            const Vector2& B = map.planets[j].pos;
            bool intersects = false;

            // Check if the segment intersects with a hostile zone
            for (const auto* hostile : map.hostile) {
                const Vector2& C = hostile->pos;
                const Vector2 D = (C - A).project(B - A) + A;

                // If D is between A and B, and it is within the hostile radius
                if (std::min(A.x, B.x) <= D.x && D.x <= std::max(A.x, B.x))
                    if ((C - D).sqr_magnitude() <= hostile->hostile_radius * hostile->hostile_radius)
                        intersects = true;
            }

            if (intersects)
                continue;

            possible_graph[i].emplace_back(j);
            possible_graph[j].emplace_back(i);

        }
    }
}