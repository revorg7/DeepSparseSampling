#include <pybind11/pybind11.h>
#include<real.h>
#include<Matrix.h>
#include "OnlineAlgorithm.h"
#include "TreeBRLPolicyPython.h"

namespace py = pybind11;


PYBIND11_MODULE(wrap2, m) {

    py::class_<OnlineAlgorithm<int, int>> base(m, "base");
//		base.def("Observe",&OnlineAlgorithm<int, int>::Observe);
		base.def("Act",&OnlineAlgorithm<int, int>::Act);
		base.def("getValue",&OnlineAlgorithm<int, int>::getValue);
//		base.def("Reset",&OnlineAlgorithm<int, int>::Reset);

 	py::class_<TreeBRLPolicyPython>(m, "derived",base)
		.def(py::init<int,int,real,int,int,int>())
		.def("Observe",py::overload_cast<int,int,real,int,int>(&TreeBRLPolicyPython::Observe))
		.def("Reset",py::overload_cast<int>(&TreeBRLPolicyPython::Reset))
    .def("saveBelief",&TreeBRLPolicyPython::saveBelief)
    .def("loadBelief",&TreeBRLPolicyPython::loadBelief)
		.def("getAction",&TreeBRLPolicyPython::getAction);
//		.def("Act",&TreeBRLPolicyPython::Act);

}


// NOte: checked create method of TreeBRLPolicyPython seperately, no problem with that
