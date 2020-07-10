
class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=================================Part I COMPLETED! ==============================================

class Stack: 
    
    def __init__(self):
        # YOU ARE NOT ALLOWED TO MODIFY THE CONSTRUCTOR
        self.top = None
        self.count=0
    
    def __str__(self):
        # YOU ARE NOT ALLOWED TO MODIFY THE THIS METHOD
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__

    def isEmpty(self):
        # YOUR CODE STARTS HERE
        return self.top == None

    def __len__(self): 
        # YOUR CODE STARTS HERE
        return self.count
        

    def push(self,value):
        # YOUR CODE STARTS HERE
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.count += 1
        

     
    def pop(self):
        # YOUR CODE STARTS HERE
        if not self.isEmpty():
            num = self.top.value
            self.top = self.top.next
            self.count -= 1
            return num
        else:
            return 'Empty Stack'
        

    def peek(self):
        # YOUR CODE STARTS HERE
        if not self.isEmpty():
            return self.top.value
        else:
            return 'Empty Stack'

#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.__expr = None

    @property
    def getExpr(self):
        return (self.__expr)

    def setExpr(self, new_expr):
        if (isinstance(new_expr, str) and len(new_expr.strip()))>0:
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None


    def isNumber(self, txt):
        if not isinstance(txt,str):
            print("Argument error in isNumber")
            return False
        # YOUR CODE STARTS HERE
        count=0
        for i in txt: 
            if i == '.': 
                count=count + 1

        if (txt.replace('.','',1).isdigit() and count==0):
            return txt+'.0'
        else:
            return False

    # TO CHECK THE TOKEN PRIORITY
    def getPriority(self, token):
        if(token=='+' or token=='-'):
            return 1
        if(token=='*' or token=='/' or token=='%'):
            return 2
        else:
            return 3

    # TO CHECK WHETEHER THE TOKEN IS OPERATOR OR NOT
    def isOperator(self, token):
        if(token=='+' or token=='-' or token=='*' or token=='/' or token=='%' or token=='^' or token=='(' or token==')'):
            return True
        else:
            return False

    # TO GET THE EXPONENT OF TWO NUMBER
    def getExponent(self, a,b):

        result=1
        while(b!= 0):
            result *= a;
            b-=1
        
        return result

    # TO SPLIT THE INFIX
    def split(self, txt):
        i=0
        while(i< len(txt)-1):
            if(self.isOperator(txt[i+1]) and txt[i]!=' 'and txt[i+2]!=' '):
                txt = txt[0:i+1]+' '+txt[i+1:i+2]+' '+txt[i+2:len(txt)]
            elif(self.isOperator(txt[i+1]) and txt[i]==' 'and txt[i+2]!=' '):
                txt = txt[0:i+2]+' '+txt[i+2:len(txt)]
            elif(self.isOperator(txt[i+1]) and txt[i]!=' 'and txt[i+2]==' '):
                txt = txt[0:i+1]+' '+txt[i+1:len(txt)]
            i-=-1

        return txt

    def check(self, myStr): 
        open_list = ["[","{","("] 
        close_list = ["]","}",")"]

        myList = [] 
        for i in myStr: 
            if i in open_list: 
                myList.append(i) 
            elif i in close_list: 
                pos = close_list.index(i) 
                if ((len(myList) > 0) and
                    (open_list[pos] == myList[len(myList)-1])): 
                    myList.pop() 
                else: 
                    return False
        if(len(myList) == 0): 
            return True
        else: 
            return False   

    def _getPostfix(self, txt):
        
        if not isinstance(txt,str) or len(txt.strip())==0:
            print("Argument error in _getPostfix")
            return None

        postfixStack=Stack()
        # YOUR CODE STARTS HERE
        checkVal=""
        for i in range(0, len(txt)):
            if(self.isOperator(txt[i])):
                checkVal=checkVal+txt[i]

        if(self.check(checkVal)):
            postfixList=[]
            txtList=[]
            postfixStack.push('(')

            txt=self.split(txt)
            txt=txt.split()

            for i in range(0, len(txt)):
                if(self.isNumber(txt[i])):
                    txt[i]=self.isNumber(txt[i])

            txt.append(')')    

            for i in range(0, len(txt)):

                if(self.isOperator(txt[i])):
                    if((postfixStack.isEmpty() or txt[i]=='(' or (self.getPriority(postfixStack.peek())<self.getPriority(txt[i]))) and (txt[i]!=')')):
                        postfixStack.push(txt[i])
                    
                    else:
                        if(txt[i]!=')'):
                            while(( not (self.getPriority(postfixStack.peek())<self.getPriority(txt[i]))) and ((postfixStack.peek()!='('))):
                                    postfixList.append(postfixStack.pop())
                            
                            postfixStack.push(txt[i])
                    
                    if(txt[i]==')'):
                        while(( not postfixStack.isEmpty()) and postfixStack.peek()!='('):
                            postfixList.append(postfixStack.pop())
                        
                        if(postfixStack.peek()=='('):
                            postfixStack.pop()
                
                else:
                    if(txt[i]!=' '):
                        postfixList.append(txt[i])
                
            while( not postfixStack.isEmpty() and postfixStack.peek()!='('):
                postfixList.append(postfixStack.pop())
            
            print('Postfix : '+' '.join(postfixList))
            
            return(postfixList)
        else:
            print('Invalid Infix')
            return None
    
    def calculate(self):

        EvalStack=Stack()
        exp=self.getExpr
        print('Infix : '+exp)

        checkVal=""
        for i in range(0, len(exp)):
            if(self.isOperator(exp[i])):
                checkVal=checkVal+exp[i]
        
        if(self.check(checkVal)):
            exp=x._getPostfix(exp)

            for i in range(0, len(exp)):
                if(not self.isOperator(exp[i])):
                    EvalStack.push(exp[i])
                else:
                    b=float(EvalStack.pop())
                    a=float(EvalStack.pop())

                    if(exp[i]=='+'):
                        result=a+b
                    elif (exp[i]=='-'):
                        result=a-b
                    elif (exp[i]=='*'):
                        result=a*b
                    elif (exp[i]=='/'):
                        result=a/b
                    elif (exp[i]=='%'):
                        result=a%b
                    elif (exp[i]=='^'):
                        result=self.getExponent(a,b)

                    EvalStack.push(result)
            
            print('Evaluation Of Postfix : ')
            print(EvalStack.pop())
            return
        else:
            print('Invalid Infix')
            return None
        
        if not isinstance(self.__expr,str) or len(self.__expr.strip())==0:
            print("Argument error in calculate")
            return None

# YOUR CODE STARTS HERE
x=Calculator()

#CHECK INFIX TO POSTFIX CONVERSION USING STACK          
x._getPostfix(' 2 ^        4')
            
# x._getPostfix('2')
            
# x._getPostfix('2.1*5+3^2+1+4.45')
            
# x._getPostfix('    2 *       5.34        +       3      ^ 2    + 1+4   ')
            
# x._getPostfix(' 2.1 *      5   +   3    ^ 2+ 1  +     4')

print('\n')            
#CHECK EVALUATION AFTER POSTFIX USING STACK           
x.setExpr('    4  +      3 -2')
x.calculate()

# x.setExpr('  2  +3.5')
# x.calculate()

# x.setExpr('4+3.65-2 /2')
# x.calculate()

# x.setExpr(' 23 / 12 - 223 +      5.25 * 4    *      3423')
# x.calculate()

# x.setExpr('   2   - 3         *4')
# x.calculate()

# x.setExpr(' 2   *  ( 4 + 2 *   (5-3^2)+1)+4')
# x.calculate()

# x.setExpr('2.5 + 3 * ( 2 +(3.0) *(5^2 - 2*3^(2) ) *(4) ) * ( 2 /8 + 2*( 3 - 1/ 3) ) - 2/ 3^2')
# x.calculate()

print('\n')
#CHECK FOR VALID INFIX 

x._getPostfix('   2 *  (  5   +   3)    ^ 2+(1  +4    ')

# x._getPostfix('2*(5 +3)^ 2+)1  +4(    ')
