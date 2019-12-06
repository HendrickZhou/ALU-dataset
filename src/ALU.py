class lazy_class_attribute:
    def __init__(self, function):
        self.fget = function

    def __get__(self, cls, A, B, op_code):
        output = self.fget(A, B, op_code)
        setattr(cls, self.fget.__name__, classmethod(self.fget))
        return output

class ALU:
    """
    Op_code:
    ********
    bit logical
    ********
    a : and
    o : or
    x : xor
   
    1ca : 1's complement of A
    1cb : 1's complemnt of B
    
    ********
    arithmetic
    ********
    ad : add
    ac : add with carry
    su : sub
    sub : sub with borrow
    msl : signed multiple lower
    msh : signed multiple higher
    mul : unsigned multiple lower
    muh : unsigned mulitple higher
    d : divide
    r : remu

    2ca : 2's complement of A
    2cb : 2's complement of B

    ia : increment A
    ib : increment B
    da : decrement A
    da : decrement B
    pa : pass A
    pb : pass B
    
    ********
    bit shift
    ********
    asla : arithmetic shift left
    asra : arithmetic shift right
    lsla : logical shift left
    lsra : logical shift right
    
    aslb : 
    asrb :
    lslb :
    lsrb :

    """

    def __init__(self, num_bit, op_code_list):
        self.op_code_list = op_code_list

    def __call__(self, A, B, op_code):
        for op in op_code:
            pass


    @lazy_class_attribute
    def AND(A, B):
        pass

    @lazy_class_attribute
    def OR(A,B):
        pass

    @lazy_class_attribute
    def XOR(A, B):
        pass

    @lazy_class_attribute
    def ADD(A, B):
        pass

    @lazy_class_attribute
    def ADDC(A, B):
        pass

    @lazy_class_attribute
    def SUB(A,B):
        pass

    @lazy_class_attribute
    def SUBB(A, B):
        pass

    




if __name__ == "__main__":
    ALU()
