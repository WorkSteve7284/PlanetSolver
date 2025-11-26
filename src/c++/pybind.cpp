#include <pybind11/pybind11.h>
#include <pybind11/operators.h>

#include "Galaxy.hpp"
#include "Vector.hpp"
#include "pybind11/detail/common.h"

namespace py = pybind11;

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
        .def(py::self / double());

    m.def("operator*", py::overload_cast<double, const Vector2&>(&operator*));

    py::enum_<ResupplyType>(m, "ResupplyType")
        .value("NONE", ResupplyType::NONE)
        .value("FOOD", ResupplyType::FOOD)
        .value("OXYGEN", ResupplyType::OXYGEN);

    py::class_<Planet>(m, "Planet")
        .def(py::init<>())
        .def(py::init<const std::string&, const Vector2&, ResupplyType, double>())
        .def(py::init<>());
}
