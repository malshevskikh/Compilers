"""
This file demonstrates a trivial function "fpadd" returning the sum of
two floating-point numbers.
"""

from llvmlite import ir

'''
#---------Класс для сложения двух операндов---------
class Sum_of_variables:
    #-----------------поля-----------------
    m = ir.Module()
    voidptr_ty = ir.IntType(8).as_pointer()
    fmt = "%d \n\0"
    c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)), bytearray(fmt.encode("utf8")))
    global_fmt = ir.GlobalVariable(m, c_fmt.type, name="fstr")
    global_fmt.linkage = 'internal'
    global_fmt.global_constant = True
    global_fmt.initializer = c_fmt
    printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
    printf = ir.Function(m, printf_ty, name="printf")

    def sum(self):
        integer = ir.IntType(32)
        fnty = ir.FunctionType(integer, ())

        func = ir.Function(m, fnty, name="main")
        # Now implement the function
        block = func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)

        result = builder.add(ir.Constant(integer, 5), ir.Constant(integer, 12), name="res")

        fmt_arg = builder.bitcast(global_fmt, voidptr_ty)
        builder.call(printf, [fmt_arg, result])
        builder.ret(result)

        print(m)
#---------------------------------------------------
'''



# --------------------------


def sum_two_parts(arg1, op, arg2):
    '''
    # Create some useful types
    double = ir.DoubleType()
    fnty = ir.FunctionType(double, ())
    
    # Create an empty module...
    #module = ir.Module(name=__file__)
    # and declare a function named "fpadd" inside it
    func = ir.Function(m, fnty, name="main")
    
    # Now implement the function
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    
    result = builder.fadd(ir.Constant(double, 1.1), ir.Constant(double, 2.1), name="res")
    #result = builder.fadd(ir.Constant(double, 1.1), ir.Constant(double, 2.1), name="res")
    fmt_arg = builder.bitcast(global_fmt, voidptr_ty)
    builder.call(printf, [fmt_arg, result])
    builder.ret(result)
    
    # Print the module IR
    print(m)
    '''

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

    #Сложение 2-х чисел типа integer
    integer = ir.IntType(32)
    fnty = ir.FunctionType(integer, ())

    func = ir.Function(m, fnty, name="main")
    # Now implement the function
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    result = None
    if op == "+":
        result = builder.add(ir.Constant(integer, arg1), ir.Constant(integer, arg2), name="res")
    elif op == "-":
        result = builder.sub(ir.Constant(integer, arg1), ir.Constant(integer, arg2), name="res")
    elif op == "*":
        result = builder.mul(ir.Constant(integer, arg1), ir.Constant(integer, arg2), name="res")
    elif op == "/":
        result = builder.sdiv(ir.Constant(integer, arg1), ir.Constant(integer, arg2), name="res")

    fmt_arg = builder.bitcast(global_fmt, voidptr_ty)
    builder.call(printf, [fmt_arg, result])
    builder.ret(result)

    #print(m)

    s = str(m).split('\n')
    s = '\n'.join(s[3:])

    with open('f1.ll', 'r+') as f:
        f.seek(0, 2)  # перемещение курсора в конец файла
        f.write(s)  # собственно, запись
