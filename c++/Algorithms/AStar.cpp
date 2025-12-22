#include "AStar.hpp"
#include "Galaxy.hpp"
#include "Path.hpp"
#include "Valid.hpp"
#include "Vector.hpp"
#include "definitions.hpp"
#include <limits>
#include <queue>
#include <vector>

struct CompareNode;

template <typename T> using min_queue = std::priority_queue<T, std::vector<T>, CompareNode>;

precision cost_all(planet_index a, planet_index b, const GalaxyMap& map) {
    const precision speed = optimal_speeds[0];
    const precision distance = (map[a].pos - map[b].pos).magnitude();
    return distance / speed + distance * (K_F * speed*speed) - 2*K_L*(distance / speed);
}

precision cost_one(planet_index a, planet_index b, const GalaxyMap& map) {
    const precision speed = optimal_speeds[1];
    const precision distance = (map[a].pos - map[b].pos).magnitude();
    return distance / speed + distance * (K_F * speed*speed) - K_L*(distance / speed);

}

precision cost_none(planet_index a, planet_index b, const GalaxyMap& map) {
    const precision speed = optimal_speeds[2];
    const precision distance = (map[a].pos - map[b].pos).magnitude();
    return distance / speed + distance * (K_F * speed*speed);

}

inline precision heuristic(planet_index a, planet_index b, const GalaxyMap& map) {
    // Best-case scenario
    //return cost_none(a, b, map);

    // Set to 0 for Djisktra's algorithm
    return 0;
}

struct Node {

    planet_index index;

    precision g_cost = std::numeric_limits<precision>::infinity();
    precision h_cost = 0;

    Node* from = nullptr;

    inline precision f_cost() const noexcept { return g_cost + h_cost; }

    struct ResupplyState {
        bool food = false, o2 = false;

        bool operator==(const ResupplyState& other) const noexcept { return food == other.food && o2 == other.o2; }

        operator unsigned char() const noexcept {
            if (food && o2)
                return 3;
            else if (food)
                return 2;
            else if (o2)
                return 1;
            else
                return 0;
        }
    } resupply;

    enum class AStarState : unsigned char {
        OPEN,
        CLOSED,
        UNKNOWN
    } state;

    inline bool operator>(const Node& other) const { return f_cost() > other.f_cost(); }

    Node(planet_index planet) : index(planet), state(AStarState::UNKNOWN)  {}
    Node() : index(-1), state(AStarState::UNKNOWN) {}
};

struct CompareNode {
    bool operator()(const Node* a, const Node* b) const {
        return *a > *b;
    }
};

std::vector<Paths::Segment> Algorithms::a_star(planet_index start, planet_index end, const GalaxyMap& map) {
    // Find segments & store graph
    Graph graph(map);

    min_queue<Node*> open;

    // Vector of map (more or less) of nodes
    std::vector<std::array<Node, 4>> nodes;

    // Populate nodes

    // Reserve # of planets
    nodes.resize(map.planets.size());

    for (planet_index i = 0; i < map.planets.size(); i++) {
        if (map[i].is_hostile)
            continue;
        nodes[i] = {Node(i), Node(i), Node(i), Node(i)};
    }

    // Add starting place to open
    open.emplace(&nodes.at(end).at(0));
    open.top()->g_cost = 0;
    open.top()->state = Node::AStarState::OPEN;

    // loop
        // current node = lowest cost in open
        // move current node from open to closed

        // if current is the target, path found

        // for each neighbor of current
            // if neighbor is closed, continue
            // if cost of neighbor is lower than old cost OR neighbor is not in open
                // Set costs
                // Set previous to current
                // if neighbor not in open
                    // Add neighbor to open

    // A* algorithm
    while (!open.empty()) {
        auto& current = *open.top();
        open.pop();

        if (current.state == Node::AStarState::CLOSED)
            continue;

        current.state = Node::AStarState::CLOSED;

        if (current.index == start)
            break;

        Node::ResupplyState target_state = current.resupply;

        if (!target_state.food && map.planets[current.index].resupply == ResupplyType::FOOD)
            target_state.food = true;
        if (!target_state.o2 && map.planets[current.index].resupply == ResupplyType::OXYGEN)
            target_state.o2 = true;

        for (auto& neighbor_index : graph.possible_graph.at(current.index)) {
            auto& neighbor = nodes.at(neighbor_index).at(target_state);

            neighbor.resupply = target_state;

            precision g_cost = current.g_cost;

            if (target_state.food && target_state.o2)
                g_cost += cost_none(current.index, neighbor_index, map);
            else if (target_state.food || target_state.o2)
                g_cost += cost_one(current.index, neighbor_index, map);
            else
                g_cost += cost_all(current.index, neighbor_index, map);

            if (g_cost < neighbor.g_cost || neighbor.state == Node::AStarState::UNKNOWN) {
                neighbor.h_cost = heuristic(neighbor_index, start, map);
                neighbor.from = &current;
                neighbor.g_cost = g_cost;
                neighbor.state = Node::AStarState::OPEN;
                open.emplace(&neighbor);
            }
        }
    }

    Node* pos = nullptr;
    precision g_cost = std::numeric_limits<precision>::infinity();
    for (auto& node : nodes.at(start))
        if (node.g_cost < g_cost) {
            pos = &node;
            g_cost = node.g_cost;
        }

    std::vector<Paths::Segment> out;

    while (pos->from) {
        precision speed;

        if (pos->resupply.food && pos->resupply.o2)
            speed = optimal_speeds[2];
        else if (pos->resupply.food || pos->resupply.o2)
            speed = optimal_speeds[1];
        else
            speed = optimal_speeds[0];

        out.emplace_back(pos->index, pos->from->index, speed);
        pos = pos->from;
    }

    return out;
}