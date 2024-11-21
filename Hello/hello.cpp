#include <nanobind/nanobind.h>
#include "Speaker.h"

NB_MODULE(hello, m) {
    nanobind::class_<Hello::Speaker>(m, "Speaker")
        .def(nanobind::init<>())
        .def("sayHello", &Hello::Speaker::sayHello);
}