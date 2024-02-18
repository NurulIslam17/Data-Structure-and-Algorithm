def create_stack():
   stack = []
   return stack


def is_empty(stack):
   return len(stack) == 0


def push(stc, item):
   stc.append(item)
   print('Last Inserted : ', item)


def delete(stack):
   if is_empty(stack):
      return 'Stack is empty'
   print('Deleted : ' + stack[-1])
   return stack.pop()


def display(stack):
   if len(stack) == 0:
      print('Stack Is Empty')
   else:
      print(stack)


if __name__ == "__main__":

   try:
      stack = create_stack()
      while True:
         option = int(input('1.Create , 2.Delete, 3.Display 4.Quit > '))
         if option == 1:
            item = int(input('Insert Item : '))
            push(stack, str(item))
         elif option == 2:
            delete(stack)
            display(stack)
         elif option == 3:
            display(stack)
         elif option == 4:
            print('Thanks :)')
            exit()
         else:
            print('Insert Correct Operation')
   except IndexError:
      print('Index Error Occurred')
