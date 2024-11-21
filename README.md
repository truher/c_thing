# c_thing

This is an experiment in c++ wrapped with python, deployed to
pypi on a schedule.

to build it:

```
$ cmake -S . -B build
$ cmake --build build
```

to run it:

```
$ cd build
$ python3
>>> import hello 
>>> x = hello.Speaker()
>>> x.sayHello()
Hello, world!
```

# notes

in CMakeLists.txt, you use nanobind_add_module(), which
has to list *all* the implementation files used for the module,
not just the "glue" file with the NB_MODULE macros in it. :-)

see https://github.com/jameskbride/cmake-hello-world

see https://nanobind.readthedocs.io/en/latest/basics.html