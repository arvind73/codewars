import re
from math import factorial as fact


def expand1(expr):
    
    a, x, b, n = re.match('\(([-]*[\d]*)([a-z])([+-][\d]+)\)\^([\d]+)',
                          expr).groups()
    if not a:
        a = 1
    elif a == '-':
        a = -1
    else:
        a = int(a)
    b, n = int(b), int(n)
    
    coefs = []
    for k in range(0, n+1):
        coefs.append(int((fact(n) / (fact(n - k) * fact(k))) * a**(n-k) * b**k))
    
    string = ''
    if len(coefs) > 2:
        for l in range(0, len(coefs)-2):
            if coefs[l] > 1:
                string += '+' + str(coefs[l]) + x + '^' + str(len(coefs) - 1 - l)
            elif coefs[l] == 1:
                string += '+' + x + '^' + str(len(coefs) - 1 - l)
            elif coefs[l] == -1:
                string += '-' + x + '^' + str(len(coefs) - 1 - l)
            elif coefs[l] < -1:
                string += str(coefs[l]) + x + '^' + str(len(coefs) - 1 - l)
    if len(coefs) > 1:
        if coefs[-2] > 1:
            string += '+' + str(coefs[-2]) + x
        elif coefs[-2] == 1:
            string += '+' + x
        elif coefs[-2] == -1:
            string += '-' + x
        elif coefs[-2] < -1:
            string += str(coefs[-2]) + x
    if coefs[-1] > 0:
        string += '+' + str(coefs[-1])
    elif coefs[-1] < 0:
        string += str(coefs[-1])
    
    return string.lstrip('+')

def expand2(expr):
    print(expr)
    #expand function takes in a equation & outputs an expression
    first_list = expr.split('^')
    print(first_list[1])
    print(first_list[0][1:len(first_list[0])-1])
    print(first_list[0][1:len(first_list[0])-1].find('-'))
    print(type(first_list[0]))
    
    def pascal_triangle(exponent):
        ret_list = []
        origin = ['1','1']
        while exponent > 1:
            ret_list = []
            prev = 0
            for i in origin:
                i = int(i)
                #so
                ret_list.append(str(i+prev))
                prev = i
            ret_list.append('1')
            exponent -= 1
            origin = ret_list
        print(ret_list)
        return ret_list
    
    if first_list[1] == '0':
        return '1'
    elif first_list[1] == '1':
        return expr[1:len(expr)-3]
        
    if first_list[0][1] == '-':
        if first_list[0][2:len(first_list[0])-1].find('-')!= -1:
            parsed = first_list[0][2:len(first_list[0])-1].split('-')
            parsed[0] = '-' + parsed[0]
            parsed[1] = '-' + parsed[1]
        else:
            parsed = first_list[0][1:len(first_list[0])-1].split('+')
    elif first_list[0].find('-')!=-1:
        parsed = first_list[0][1:len(first_list[0])-1].split('-')
        parsed[1] = '-'+parsed[1]
    else:
        parsed = first_list[0][1:len(first_list[0])-1].split('+')
    
    print(parsed)
    exponential = int(first_list[1])
    first_ret = []
    second_ret = []
    ret_list = pascal_triangle(exponential)
    if len(parsed[0]) > 1:
        #check the constant here
        print(parsed[0])
        splitted = re.split('[a-z]',parsed[0])
        print('look at this')
        print(splitted)
        #for the minus number
        if splitted[0]=='-':
            splitted[0] = '-1'
        splitted[1] = parsed[0][-1]
        a = splitted
        print(a)
        b = parsed[1]
        current_exponential = exponential
        current_second_exponential = 0
        real_list = []
        for each_term in ret_list:
            i = int(each_term)
            added = i*(int(splitted[0])**current_exponential)*int(int(b)**current_second_exponential)
            print(added)
            print('sup boiz')
                
            if current_exponential == 1:
                added = str(added)+splitted[1]
            elif current_exponential == 0:
                added = str(added)
            else:
                added = str(added)+splitted[1]+'^'+str(current_exponential)
            real_list.append(added)
            print(added)
            current_second_exponential += 1
            current_exponential -= 1
        ret_string = ''
        counter = 0
        for i in real_list:
            if counter == 0:
                counter += 1
                #what is this for the first term?
                #if len(i) < 3:
                #    if i[0] == '1':
                #        i = i[1:len(i)-1]
                ret_string += i
                continue
            if i[0] != '-':
                i = '+'+i
            ret_string += i
        return ret_string
        #do the following
    else:
        print(parsed)
        a = parsed[0]
        b = parsed[1]
        current_exponential = exponential
        current_second_exponential = 0
        real_list = []
        for each_term in ret_list:
            i = int(each_term)
            added = i*int(int(b)**current_second_exponential)
            if current_exponential == 1:
                added = str(added)+a
            elif current_exponential == 0:
                added = str(added)
            else:
                added = str(added)+a+'^'+str(current_exponential)
            real_list.append(added)
            print(added)
            current_second_exponential += 1
            current_exponential -= 1
        ret_string = ''
        counter = 0
        for i in real_list:
            if counter == 0:
                counter += 1
                if i[0] == '1':
                    i = i[1:len(i)]
                ret_string += i
                continue
            if i[0] != '-':
                i = '+'+i
            ret_string += i
        return ret_string
        return 1
        #do the easier way
    
    print(parsed)
    pass


from math import factorial as f
def ncr(n,r): return f(n)//(f(r)*f(n-r))
def expand3(expr):
    l1=expr.split('^')
    n=int(l1[-1])
    if n==0: return '1'
    l1=l1[0].strip('(').strip(')')
    if n==1: return l1
    if '+' in l1:
      l2=l1.split('+')
      b=int(l2[-1])
      var=l2[0][-1]
      if len(l2[0])==1: a=1
      elif len(l2[0])==2 and l2[0][0]=='-': a=-1
      else: a=int(l2[0][:-1])
    else:
      flg=l1[0]=='-'
      l2=l1.split('-')
      b=-int(l2[-1])
      var=l2[-2][-1]
      if flg:
        if len(l2[-2])==1: a=-1
        else: a=-int(l2[-2][:-1])
      else:
        if len(l2[-2])==1: a=1
        else: a=int(l2[-2][:-1])
    cf=[ncr(n,r)*(a**(n-r))*(b**r) for r in range(n+1)]
    s='+'.join(str(cf[r])+var+'^'+str(n-r) for r in range(n-1) if cf[r]!=0)
    if cf[-2]!=0: s=s+'+'+str(cf[-2])+var
    if cf[-1]!=0: s+='+'+str(cf[-1])
    res=s.replace('+-','-').replace('+1'+var,'+'+var).replace('-1'+var,'-'+var)
    if res[:2]=='1'+var: res=res[1:]
    return res
    

print(expand3("(x+10)^2"))