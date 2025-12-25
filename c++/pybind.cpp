#include "Algorithms/AStar.hpp"
#include "Galaxy.hpp"
#include "Path.hpp"
#include "Vector.hpp"
#include "definitions.hpp"

#include <pybind11/pybind11.h>
#include <pybind11/operators.h>
#include <pybind11/stl.h>

namespace py = pybind11;

PYBIND11_MODULE(planetsolver, m) {
    m.doc() = "C++ code for PlanetSolver";

    py::class_<Vector2>(m, "Vector2")
        .def(py::init<>())
        .def(py::init<double, double>())
        .def_readwrite("x", &Vector2::x)
        .def_readwrite("y", &Vector2::y)
        .def("sqr_magnitude", &Vector2::sqr_magnitude)
        .def("magnitude", &Vector2::magnitude)
        .def("project", &Vector2::project)
        .def(py::self + py::self)
        .def(py::self - py::self)
        .def(py::self * 1.0)
        .def(py::self += py::self)
        .def(py::self -= py::self)
        .def(py::self == py::self)
        .def(py::self != py::self);

    py::class_<Planet>(m, "Planet")
        .def(py::init<std::string, Vector2, ResupplyType, precision, bool>())
        .def_readwrite("pos", &Planet::pos)
        .def_readwrite("name", &Planet::name)
        .def_readwrite("resupply", &Planet::resupply)
        .def_readwrite("hostile_radius", &Planet::hostile_radius)
        .def_readwrite("is_hostile", &Planet::is_hostile);

    py::class_<GalaxyMap>(m, "GalaxyMap")
        .def(py::init<planet_index>())
        .def("add_planet", &GalaxyMap::add_planet)
        .def("index_from_name", &GalaxyMap::index_from_name)
        .def_readwrite("planets", &GalaxyMap::planets);

    py::enum_<ResupplyType>(m, "ResupplyType")
        .value("NONE", ResupplyType::NONE)
        .value("FOOD", ResupplyType::FOOD)
        .value("OXYGEN", ResupplyType::OXYGEN);

    auto m_paths = m.def_submodule("paths");

    py::class_<Paths::Segment>(m_paths, "Segment")
        .def(py::init<planet_index, planet_index, precision>())
        .def_readwrite("start", &Paths::Segment::start)
        .def_readwrite("end", &Paths::Segment::end)
        .def_readwrite("speed", &Paths::Segment::speed);

    m.def("find_best_path", &Algorithms::a_star);

}