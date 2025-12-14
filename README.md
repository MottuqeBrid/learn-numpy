# NumPy Playground

Small collection of NumPy practice scripts illustrating array creation, data types, basic operations, and random number utilities.

## Project layout

- [main.py](main.py): demonstrates 1D/2D/3D arrays, dimensionality, and simple statistics like mean.
- [array.py](array.py): compares Python list vs NumPy array performance with a tiny timing example.
- [arrayOpereations.py](arrayOpereations.py): elementwise arithmetic (add, subtract, multiply, divide, power, modulus) plus reciprocals for 1D and 2D arrays.
- [DataType.py](DataType.py): shows how NumPy infers and converts dtypes (ints, floats, strings, bools, complex) and how to set explicit dtype.
- [zeroArray.py](zeroArray.py): builds zeros/ones/empty arrays, identity/diagonal matrices, `arange`, and `linspace` examples.
- [createArryWithRandomNumber.py](createArryWithRandomNumber.py): random sampling with `rand`, `randn`, `ranf`, and `randint` for 1D/2D arrays.
- [ArathmaticOperation.py](ArathmaticOperation.py): min/max operations, indexing with `argmin`/`argmax`, square root, standard deviation, cumulative sum, and trigonometric functions.
- [arrayFunction2.py](arrayFunction2.py): array manipulation including shuffle, unique elements, resize, flatten, and ravel operations.
- [broadcasting.py](broadcasting.py): demonstrates NumPy broadcasting rules for arrays with different shapes.
- [copyVsView.py](copyVsView.py): illustrates the difference between copying arrays and creating views in NumPy.
- [InsertAndDelete.py](InsertAndDelete.py): insert, append, and delete operations for 1D and 2D arrays.
- [iterating.py](iterating.py): demonstrates different ways to iterate through arrays using loops, `nditer`, and `ndenumerate`.
- [jointAndSplit.py](jointAndSplit.py): concatenate, stack, and split arrays using `concatenate`, `stack`, and `array_split`.
- [matrix.py](matrix.py): matrix operations including multiplication, transpose, inverse, determinant, eigenvalues, and other linear algebra functions.
- [shape.py](shape.py): explores array shapes, reshaping arrays, and the `ndmin` parameter.
- [slicing.py](slicing.py): demonstrates array indexing and slicing for 1D and 2D arrays.

## How to run

1. Ensure Python and NumPy are installed: `pip install numpy`.
2. From the project directory, run any script, e.g. `python main.py`.

## Notes

- Scripts print results directly; no inputs are required.
- These examples aim for clarity over performance or structure—feel free to adapt them into functions or notebooks as you experiment.
