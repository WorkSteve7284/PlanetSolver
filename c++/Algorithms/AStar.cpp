#include "AStar.hpp"
#include "Galaxy.hpp"
#include "Path.hpp"
#include "Valid.hpp"
#include "Vector.hpp"
#include "definitions.hpp"
#include <algorithm>
#include <vector>

precision cost_all(planet_index a, planet_index b, const GalaxyMap& map) {
    const precision distance = (map[a].pos - map[b].pos).magnitude();
    return distance / optimal_speeds[2] + distance * (K_F * optimal_speeds[2] * optimal_speeds[2]) - 2*K_L*(distance / optimal_speeds[2]);
}

precision cost_one(planet_index a, planet_index b, const GalaxyMap& map) {
    const precision distance = (map[a].pos - map[b].pos).magnitude();
    return distance / optimal_speeds[1] + distance * (K_F * optimal_speeds[1] * optimal_speeds[1]) - K_L*(distance / optimal_speeds[1]);

}

precision cost_none(planet_index a, planet_index b, const GalaxyMap& map) {
    const precision distance = (map[a].pos - map[b].pos).magnitude();
    return distance / optimal_speeds[0] + distance * (K_F * optimal_speeds[0] * optimal_speeds[0]);

}

precision heuristic(planet_index n, planet_index target, const GalaxyMap& map) {
    const precision distance = (map[target].pos - map[n].pos).magnitude();
    // Best-case scenario
    return distance / optimal_speeds[0] + distance * (K_F * optimal_speeds[0] * optimal_speeds[0]);
}

std::vector<Paths::Segment> Algorithms::a_star(planet_index start, planet_index end, const GalaxyMap& map) {
    // Find segments
    const Graph graph(map);

    // Traverse backwards
    std::vector<planet_index> history = {end};
    std::vector<Paths::Segment> out;

    planet_index pos = end;

    bool resupplied_o2 = false;
    bool resupplied_food = false;

    while (pos != start) {

        precision est_cost = 10'000;
        unsigned char speed = 0;
        planet_index next_planet = 0;

        for (auto& option : graph[pos]) {

            if (std::find(history.begin(), history.end(), option) != history.end())
                continue;

            const precision h = heuristic(option, start, map);

            if (resupplied_food && resupplied_o2) {
                if (h + cost_none(pos, option, map) < est_cost) {
                    est_cost = h + cost_none(pos, option, map);
                    next_planet = option;
                    speed = 2;
                }
            }

            else if (resupplied_food ||  resupplied_food) {
                if (h + cost_one(pos, option, map) < est_cost) {
                    est_cost = h + cost_one(pos, option, map);
                    next_planet = option;
                    speed = 1;
                }
            }

            else {
                if (h + cost_all(pos, option, map) < est_cost) {
                    est_cost = h + cost_all(pos, option, map);
                    next_planet = option;
                    speed = 0;
                }
            }
        }

        out.emplace_back(next_planet, pos, optimal_speeds[speed]);
        pos = next_planet;
        history.emplace_back(next_planet);


        if (map[pos].resupply == ResupplyType::FOOD)
            resupplied_food = true;
        if (map[pos].resupply == ResupplyType::OXYGEN)
            resupplied_o2 = true;

    }

    std::reverse(out.begin(), out.end());

    return out;
}