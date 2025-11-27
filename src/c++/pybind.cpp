#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/operators.h>
#include <pybind11/detail/common.h>

#include <string>

#include "Galaxy.hpp"
#include "Path.hpp"
#include "Resources.hpp"
#include "Vector.hpp"


namespace py = pybind11;


// Bindings for pybind11 (python interface)
PYBIND11_MODULE(planetsolver_cxx, m) {
    m.doc() = "C++ Interface for PlanetSolver"; // optional module docstring

    py::class_<Vector2>(m, "Vector2")
        .def(py::init<>())
        .def(py::init<double, double>())
        .def(py::init<double, double>())
        .def("sqr_magnitude", &Vector2::sqr_magnitude)
        .def("magnitude", &Vector2::magnitude)
        .def("normalized", &Vector2::normalized)
        .def("normalize", &Vector2::normalize)
        .def(py::self == py::self)
        .def(py::self != py::self)
        .def(py::self + py::self)
        .def(py::self - py::self)
        .def(py::self * double())
        .def(py::self / double())
        .def("__str__", &Vector2::operator std::string)
        .def_readwrite("x", &Vector2::x)
        .def_readwrite("y", &Vector2::y);

    m.def("operator*", py::overload_cast<double, const Vector2&>(&operator*));

    py::enum_<ResupplyType>(m, "ResupplyType")
        .value("NONE", ResupplyType::NONE)
        .value("FOOD", ResupplyType::FOOD)
        .value("OXYGEN", ResupplyType::OXYGEN);

    py::class_<Planet>(m, "Planet")
        .def(py::init<>())
        .def(py::init<const std::string&, const Vector2&, ResupplyType, double>())
        .def(py::init<const std::string&, const Vector2&, ResupplyType, double, bool>())
        .def_readwrite("name", &Planet::name)
        .def_readwrite("index", &Planet::index)
        .def_readwrite("position", &Planet::position)
        .def_readwrite("resupply", &Planet::resupply)
        .def_readwrite("hostile_radius", &Planet::hostile_radius)
        .def_readwrite("is_hostile", &Planet::is_hostile);

    py::class_<GalaxyMap>(m, "GalaxyMap")
        .def(py::init<>())
        .def("add_planet", &GalaxyMap::add_planet)
        .def_readwrite("index_to_name", &GalaxyMap::index_to_name)
        .def_readwrite("name_to_index", &GalaxyMap::name_to_index)
        .def_readwrite("planets", &GalaxyMap::planets);

    py::class_<Resources>(m, "Resources")
        .def_readwrite("food", &Resources::food)
        .def_readwrite("oxygen", &Resources::oxygen)
        .def_readwrite("fuel", &Resources::fuel);

    py::class_<PathSegment>(m, "PathSegment")
        .def_readwrite("start", &PathSegment::start)
        .def_readwrite("end", &PathSegment::end)
        .def_readwrite("speed", &PathSegment::speed);
}
