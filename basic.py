#importing pack.py program to basic.py program
import pack
#take input from console
s = input("enter what you want to search:  ")
print(f'{s} >>>')
#split the entered input to word by word
s=s.split()
# iteration starts for searching the keyword
i=int(0)
while i<len(s):
    key = s[i]
    if key == 'oop' or key == 'oops' or key == 'java':
       print(pack.oop())
    if key == 'attributes' or key == 'encapsulation' or key == 'polymorphism' or key == 'inheritance':
        print(pack.attributes_oop())
    if key == 'sample' or key == 'program':
        print(pack.sample())
    if key == 'identifier' or key == 'identifiers':
        print(pack.identifier())
    if key == 'keyword' or key == 'keywords':
        print(pack.keyword())
    if key == 'operator' or key == 'operators':
        print(pack.operator())
    if key == 'arithmetic':
        print(pack.arithmetic())
    if key == 'assignment':
        print(pack.assignment())
    if key == 'unary':
        print(pack.unary())
    if key == 'relational':
        print(pack.relational())
    if key == 'logical':
        print(pack.logical())
    if key == 'boolean':
        print(pack.boolean())
    if key == 'bitwise':
        print(pack.bitwise())
    if key == 'ternary' or key == 'conditional':
        print(pack.ternary())
    if key == 'member':
        print(pack.member())
    if key == 'instance':
        print(pack.instance())
    if key == 'new':
        print(pack.new())
    if key == 'cast':
        print(pack.cast())
    if key == 'priority':
        print(pack.priority())
    if key == 'datatype' or key == 'datatypes':
        print(pack.datatype())
    if key == 'variable':
        print(pack.variable())
    if key == 'string' or key == 'strings':
        print(pack.string())
    if key == 'handling':
        print(pack.handling())

    i=i+1
#end of the program
