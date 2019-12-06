# ALU-dataset
Dataset for simulating Arithmetic Logic Unit\

##Format of our dataset
follow the same convention of [CIFAR-10 and CIFAR-100](https://www.cs.toronto.edu/~kriz/cifar.html)\
Datas are stored in the form of pickle object\
After unpickling the data we get a dictionary of 'data' and 'label'.
'data' will be a list of int 0/1, following the order like this:
[0,1...0,1, //input A
 1,1...0,0, //input B
 1,0,        //opcode
]

To make things simpler, only support 3 types of ops, and only support integer:\
> Arithmetic operations\
> Bitwise logical operations\
> Bit shift operations\


class `ALU` will simulate the calculation process


Expected excuation method:
`bit_arr_in_1, bit_arr_in_2, bit_op_code, bit_arr_out = ALU(decimal_1, decimal_2, decimal_op_code)`
