# c_thing

This is an experiment in c++ wrapped with python, deployed to
pypi on a schedule.

see https://github.com/jameskbride/cmake-hello-world

see https://nanobind.readthedocs.io/en/latest/basics.html

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