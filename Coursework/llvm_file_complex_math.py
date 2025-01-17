import os

"""
This file demonstrates a trivial function "fpadd" returning the sum of
two floating-point numbers.
"""


from llvmlite import ir

# print(arg1, arg2)
m = ir.Module()

# --------------------------
voidptr_ty = ir.IntType(8).as_pointer()
fmt = "%d \n\0"
c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)), bytearray(fmt.encode("utf8")))
global_fmt = ir.GlobalVariable(m, c_fmt.type, name="fstr")
global_fmt.linkage = 'internal'
global_fmt.global_constant = True
global_fmt.initializer = c_fmt
printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
printf = ir.Function(m, printf_ty, name="printf")


def complex_math_three_objects(arg1, op, arg2):
    print("опа")
    print(arg1, op, arg2)
    for i in arg1:
        print(i, type(i))
    print(op, type(op))
    print(arg2, type(arg2))

    #Сложение 2-х чисел типа integer
    integer = ir.IntType(32)
    fnty = ir.FunctionType(integer, ())

    func = ir.Function(m, fnty, name="main")

    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)

    result1 = None
    if arg1[1] == "+":
        result1 = builder.add(ir.Constant(integer, arg1[0]), ir.Constant(integer, arg1[2]), name="res")
    elif arg1[1] == "-":
        result1 = builder.sub(ir.Constant(integer, arg1[0]), ir.Constant(integer, arg1[2]), name="res")
    elif arg1[1] == "*":
        result1 = builder.mul(ir.Constant(integer, arg1[0]), ir.Constant(integer, arg1[2]), name="res")
    elif arg1[1] == "/":
        result1 = builder.sdiv(ir.Constant(integer, arg1[0]), ir.Constant(integer, arg1[2]), name="res")

    print('result1', result1)

    #s = os.system('lli ')

    final_result = None

    if op == "+":
        final_result = builder.add(ir.Constant(integer, result1), ir.Constant(integer, arg2), name="res")
    elif op == "-":
        final_result = builder.sub(ir.Constant(integer, result1), ir.Constant(integer, arg2), name="res")
    elif op == "*":
        final_result = builder.mul(ir.Constant(integer, result1), ir.Constant(integer, arg2), name="res")
    elif op == "/":
        final_result = builder.sdiv(ir.Constant(integer, result1), ir.Constant(integer, arg2), name="res")


    fmt_arg = builder.bitcast(global_fmt, voidptr_ty)
    builder.call(printf, [fmt_arg, final_result])
    builder.ret(final_result)


    s = str(m).split('\n')
    s = '\n'.join(s[3:])

    print(m)

    with open('f2.ll', 'r+') as f:
        f.seek(0, 2)  # перемещение курсора в конец файла
        f.write(s)  # собственно, запись