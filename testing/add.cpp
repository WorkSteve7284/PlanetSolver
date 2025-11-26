#include <pybind11/pybind11.h>

namespace py = pybind11;


class Adder {
  public:

    Adder() = default;

    int add(int i, int j) {
        return i + j;
    }
};

PYBIND11_MODULE(example, m, py::mod_gil_not_used()) {
    m.doc() = "pybind11 example plugin"; // optional module docstring

    py::class_<Adder>(m, "Adder")
        .def(py::init<>())
        .def("add", &Adder::add);
}
