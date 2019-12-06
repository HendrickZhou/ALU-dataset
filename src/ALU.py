# class lazy_class_attribute:
#     def __init__(self, function):
#         self.fget = function

#     def __get__(self, cls, A, B, op_code):
#         output = self.fget(A, B, op_code)
#         setattr(cls, self.fget.__name__, classmethod(self.fget))
#         return output

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
    # msl : signed multiple lower
    # msh : signed multiple higher
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

    def __init__(self, num_bit = 8, op_code_list = ['ad', 'ac', 'su', 'a', 'o', 'x']):
        self.op_dict = {
            'ad' : self.ADD,
            'ac' : self.ADDC,
            'su' : self.SUB,
            # 'sub' : self.SUBB,
            'a' : self.AND,
            'o' : self.OR,
            'x' : self.XOR,
        }
        self.bits = num_bit
        self.op_code_list = op_code_list
        self.op_code_len = self.op_code_list.__len__().bit_length()
        op_bits = []
        meta_dic = dict()
        for i in range(len(op_code_list)):
            op_bits.append(self.toNBit(i+1, self.op_code_len))
            meta_dic[self.toNBit(i+1, self.op_code_len)] = op_code_list[i]
        self.op_bits = op_bits
        self.meta_dic = meta_dic

    def __call__(self, A, B, op_code):
        if not self._valid_input(A) or not self._valid_input(B):
            raise Exception("input out of range")
        if op_code not in self.op_dict:
            raise Exception("Illegal op_code")
        return self.op_dict[op_code](A, B)

    def _valid_input(self, inputd):
        if inputd.bit_length() > self.bits or inputd < 0:
            return False
        return True

    def AND(self, A, B):
        return self.toNBit(A & B)

    def OR(self,A,B):
        return self.toNBit(A | B)

    def XOR(self,A, B):
        return self.toNBit(A ^ B)

    def ADD(self,A, B):
        return self.toNBit(A + B)

    def ADDC(self,A, B):
        return self.toNBit(A+B+1)

    def SUB(self,A,B):
        return self.toNBit(A-B)

    # def SUBB(self,A, B):
    #     return self.toNBit(A-B)

    def gen_range(self):
        # give the bit, generate the decimal range for us
        low = 0
        high = int('1' * self.bits, 2)
        return range(low, high + 1)
    
    def toNBit(self, number, bits=None):
        if not bits:
            if number > 0:
                b =  bin(number)[2:][-self.bits:]
                if number.bit_length() < self.bits:
                    return (self.bits - number.bit_length())*'0' + b
                else:
                    return b
            else:
                min_bits = max(self.bits, number.bit_length())
                return bin(number + (1<<min_bits))[2:][-self.bits:]

        else:
            if number > 0:
                b =  bin(number)[2:][-bits:]
                if number.bit_length() < bits:
                    return (bits - number.bit_length())*'0' + b
                else:
                    return b
            else:
                min_bits = max(bits, number.bit_length())
                return bin(number + (1<<min_bits))[2:][-bits:]           


if __name__ == "__main__":
    dumbALU = ALU()
    print(dumbALU.meta_dic)
    for n in dumbALU.gen_range():
        for m in dumbALU.gen_range():
            print(dumbALU(n, m, 'a'))

