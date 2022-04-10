#include<iostream>
#include<conio.h>
using namespace std;
class Stack
{
private:
    int top =0;
    int arr[5];

public:
    Stack() // calling a default constructor
    {
        top=-1;
        for(int i=0; i<5; i++)
        {
            arr[i]=0; // set all value 0 initially
        }
    }

    bool isEmpty()  // Checking whether stack is empty or not
    {
        if(top==-1)
            return true;
        else
            return false;
    }
    bool isFull()
    {
        if(top==4)
            return true;
        else
            return false;
    }

    void push(int val)
    {
        if(isFull())
            cout<<"Stack Overflow"<<endl;
        else
        {
            top++;
            arr[top]=val;
        }
    }

    int pop()
    {
        if(isEmpty())
        {
            cout<<"Stack Underflow"<<endl;
            return 0;
        }
        else
        {
            int popVal = arr[top];
            arr[top]=0;
            top--;
            return popVal;
        }

    }
    int count()
    {
        return (top+1);
    }
    int peek(int pos)
    {
        if(isEmpty())
        {
            cout<<"Stack Underflow"<<endl;
            return 0;
        }
        else
        {
            return arr[pos];
        }
    }
    void change(int pos, int val)
    {
        arr[pos]=val;
        cout<<"Value Changes in location "<<pos<<endl;
    }
    void display()
    {
        cout<<"All value in a stack are : "<<endl;
        for(int i=4; i>=0; i--)
        {
            cout<<arr[i]<<endl;
        }
    }
};

int main()
{
    Stack s;

    int option,pos,val;

    do
    {
        cout<<"Select Option Number for the operation : \n";
        cout<<"1.PUSH"<<endl;
        cout<<"2.POP"<<endl;
        cout<<"3.isEMPTY"<<endl;
        cout<<"4.isFULL"<<endl;
        cout<<"5.PEEK"<<endl;
        cout<<"6.COUNT"<<endl;
        cout<<"7.CHANGE"<<endl;
        cout<<"8.DISPLAY"<<endl;
        cout<<"9.CLEAR"<<endl;
        cout<<"0.EXIT"<<endl;

        cin>>option;
        switch(option)
        {
        case 0:
            break;
        case 1:
            cout<<"Enter the item to push : ";
            cin>>val;
            s.push(val);
            break;

        case 2:
            cout<<"Enter the item to push is "<<s.pop()<<endl;
            break;

        case 3:
            if(s.isEmpty())
                cout<<"Stack is empty."<<endl;
            else
                cout<<"Stack is not empty."<<endl;
            break;

        case 4:
            if(s.isFull())
                cout<<"Stack is Full."<<endl;
            else
                cout<<"Stack is not full."<<endl;
            break;

        case 5:
            cout<<"Enter the position from where u want to pick value : ";
            cin>>pos;
            cout<<"Pick value is "<<s.peek(pos)<<endl;;
            break;

        case 6:
            cout<<"Total values are" << s.count()<<endl;
            s.push(val);
            break;

        case 7:
            cout<<"Enter the position to change : ";
            cin>>pos;
            cout<<"Enter the value to change : ";
            cin>>val;
            s.change(pos,val);
            cout<<"Change Function is called"<<endl;
            break;

        case 8:
            cout<<"All values : "<<endl;
            s.display();
            break;
        case 9:
            system("cls");
            break;
        default:
            cout<<"Enter the proper option number"<<endl;
        }
    }
    while(option!=0);
}
