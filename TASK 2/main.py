
from MathOperation.addOp import addValue
from MathOperation.subOp import subValue

# from 'foldername'.'filename' import 'function name'

if __name__ == '__main__':
   print("this is main code")
   val1 = int(input("enter first number "))
   val2 = int(input("enter second number "))
   op = input('which math op you want to do ?')

if op.lower() == 'add':
   a1 = addValue(val1,val2)
   print(f'addition = {a1}')
elif op.lower() == 'sub':
   a2 = subValue(val1,val2)
   print(f'substarct = {a2}')
else:
   print('please choose correct operation, add, sub')