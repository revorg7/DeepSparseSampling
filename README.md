# PYTHON API for the paper "Bayesian Reinforcement Learning via Deep,Sparse Sampling, AISTATS 2020"

* This code serves as Python API for using the original c++ implementation used in the paper. 
* The original c++ implementation of the DSS algorithm as described in the paper, is part of a larger Bayesian reinforcement learning library (Dimitrakakis, Christos, Tziortziotis, Nikolaos, and Tossou, Aristide. Beliefbox: A framework for statistical methods in sequential decision making. http://code.google.com/p/beliefbox/, 2007). 
* The DSS algorithm is published under the header "TreeBRLPolicy.h" in algorithms folder of author's own fork (https://github.com/revorg7/beliefbox).
* To target larger audience, by using Pybind11 (Jakob W, Rhinelander J, Moldovan D. pybind11–Seamless operability between C++ 11 and Python.), the author provides compiled shared library (.so) which can be imported directly from standard(CPython) python3 in Linux systems (tested Python 3.6.9, Ubuntu 18.04.1).
* This API was used in conjuction with Bsuite environment API by Deepmind (Osband, Ian, et al. "Behaviour suite for reinforcement learning." arXiv preprint arXiv:1908.03568 (2019).) to draw the Regret plots comparing DSS to BDQN (Bootstrapped DQN) and TS (Thompson sampling) in Appendix-D of our submission (cf. supplementary file).
* One is always free to reproduce the main results of the paper by directly using the C++ implementation of beliefbox, which also implements various RL environments.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* bsuite (https://github.com/deepmind/bsuite)
* Pandas (>= 0.25.3)
* GNU parallel (Tange O. Gnu parallel-the command-line power tool. The USENIX Magazine. 2011 Feb;36(1):42-7.). You only need need this if you are running multiple instances of a python-script in parallel (which we do here for convenience).

### Extra information
* You don't need to install beliefbox though, unless you want to play with c++ implementation directly, or compile the ".so" files using Pybind11. You can just import the compiled binaries directly in this instance. 

* If you want check under the hood anyways, you must familiarize yourself with beliefbox in general, and DSS algorithm "TreeBRLPolicyPython.h" in particular. This class implements the DSS algorithm same as "TreeBRLPolicy.h" but also acts as a wrapper to properly use it with Pybind11. Finally, you can compile the corresponding "wrap2.cc" to get your custom Python library(*.so) for any beliefbox algorithm in general.


### Setting up your local machine

* You need to understand that the compiled "*.so" are called by Python3 only if they are avaiallbe in its path. So you must set the LD_LIBRARY_PATH to include the path to "sharedlibs" folder which contains the necessary dependencies:

```
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/..PathTo..sharedlibs
```


* The DSS algorithm can be access by importing wrap2 directly from your Python script. It contains a class called "derived" which is basically a Pybind11 interface to the c++ class "TreeBRLPolicyPython.h". The exact API is declared in wrap2.cc which can be used as reference. Although you don't need that, because the test-script "testDeepsea_episodic.py" calls and uses the API appropriately alongside any RL environment. Below is an example of its initialization:

```python
from wrap2 import derived

ql = derived(n_size*n_size,n_actions,discount,2,5,40)
```

* This initializes the DSS algorithm with state size, action size, discount factor, and (N,M,K) parameter tuple as detailed in the paper. The 'H' parameter is set to 1 for this particular "wrap2.so", so you don't need to set it during declaration. There are two additional '*.so' files, namely "wrap2-H1.so" and "wrap2-H2.so" which have 'H' parameter set as 1 and 2 respectively. You just need to rename them "wrap2.so" and paste in the root directory to use them instead. 

* Similary, we have "wrap2-TS.so", which implements beliefbox version of TS. To use this, just rename and replace "wrap2.so" in root directory with this one. Then change the derived class declaration to the following in "testDeepsea_episodic.py":

```python
from wrap2 import derived

ql = derived(n_size*n_size,n_actions,discount)
```

## Running the tests

* "testDeepsea_episodic.py" uses DSS algorithm on Deepsea environment. It takes a seed value for the environment as input. We compare it by plotting Regret against BDQN (Bootstrapped DQN) and TS (Thompson sampling) algorithms on the same environment.

* Each scipt is called multiple number of times with random (but fixed) seed values, using the script "test_all.sh". This uses GNU parallel to run multiple instances essentially. This is the only place where GNU parallel is used, and can be removed from dependencies, if you find have suitable way to run multiple experiments.

* The folder "other-codes" also gives the "testDeepsea_BDQN.py" script to run BDQN algorithm on Deepsea environment, along with other non-essential codes.

The results from experiments are then stored in SAVE_PATH_RAND folder, which can then be parsed using "plotter.py" to get plots.

* The final Regret plots are given in 'finalPlots' folder for reference. These are the ones used in Appendix-D of the paper.

## Conclusion/Summary

* The whole exercise of selecting bsuite library and Deepsea environment was to demonstrate the reusability of our implementation, as well as reproducibility of DSS's advantage over current SOTA.

* On note of comparision to SOTA, it has been noted in "Making Sense of Reinforcement Learning and Probabilistic Inference, ICLR 2020" that TS, K-learning and BDQN fair extremely similar in practice. And although not directly comparable, DSS Regret performance is shown here to be better than TS and BDQN for discrete grid-world environments (upto 20x20 atleast).

## Cite

You can cite "Grover, D., Basu, D., & Dimitrakakis, C. (2019). Bayesian Reinforcement Learning via Deep, Sparse Sampling. arXiv preprint arXiv:1902.02661." if this repository has been useful to you.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## References

* Dimitrakakis, Christos, Tziortziotis, Nikolaos, and Tossou, Aristide. Beliefbox: A framework for statistical methods in sequential decision making. http://code.google.com/p/beliefbox/, 2007.
* Jakob W, Rhinelander J, Moldovan D. pybind11–Seamless operability between C++ 11 and Python.
* Osband, Ian, et al. "Behaviour suite for reinforcement learning. CoRR, abs/1908.03568, 2016." (1908).
* Tange O. Gnu parallel-the command-line power tool. The USENIX Magazine. 2011 Feb;36(1):42-7.

