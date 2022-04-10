#include<iostream>
#include<conio.h>
#include<bits/stdc++.h>
using namespace std;
class Queue
{
private:
    int font;
    int rear;
    int arr[5];

public:
    Queue()
    {
        font = -1;
        rear = -1;
        for(int i=0; i<5; i++)
        {
            arr[i]=0;
        }
    }
    bool isEmpty()
    {
        if(font==-1 && rear==-1)
            return true;
        else
            return false;
    }
    bool isFull()
    {
        if(rear == sizeof(arr)-1)
            return true;
        else
            return false;
    }

    void enQueue(int value)
    {
        if(isFull())
        {
            cout<<"Queue is full"<<endl;
            return;
        }
        else if(isEmpty())
        {
            font=0;
            rear=0;
            arr[rear]=value;
        }
        else
        {
            rear++;
            arr[rear]=value;
        }
    }
    int deQueue()
    {
        int x;
        if(isEmpty())
        {
            cout<<"Queue is Empty"<<endl;
            return 0;
        }
        else if(font==rear) // for first index............. where raer =0 and font = 0
        {
            x=arr[font];
            arr[font]=0;
            font=-1;
            rear=-1;
            return x;
        }
        else
        {
            x=arr[font];
            arr[font]=0;
            font++;
            return x;
        }

    }
    int count()
    {
        return(rear - font+1);
    }

    void display()
    {
        cout<<"All values in the queues are : \n";
        for(int i=0; i<5;i++)
        {
            cout<<arr[i]<<" ";
        }
        cout<<endl;
    }

};


int main()
{
    Queue q1;
    int operation, pos,val;
    do
    {
        cout<<"1. Enqueue"<<endl;
        cout<<"2. Dequeue"<<endl;
        cout<<"3. IsEmpty"<<endl;
        cout<<"4. IsFull"<<endl;
        cout<<"5. Count"<<endl;
        cout<<"6. Display"<<endl;
        cout<<"7. Clear"<<endl;

        cin>>operation;
        switch(operation)
        {
            case 0:
                break;

        case 1:
            cout<<"Enter the value you wat to enqueue :";
            cin>>val;
            q1.enQueue(val);
            break;

        case 2:
            cout<<"Deque Operation\n Value is :"<<q1.deQueue()<<endl;
            break;
        case 3:
            if(q1.isEmpty())
                cout<<"Queue is Empty"<<endl;
            else
               cout<<"Queue is not Empty"<<endl;
            break;
        case 4:
            if(q1.isFull())
                cout<<"Queue is full"<<endl;
            else
                cout<<"Queue is not full"<<endl;
            break;
        case 5:
            cout<<"Total  element is : "<<q1.count()<<endl;
            break;
        case 6:
            q1.display();
            break;
        case 7:
            system("cls");
            break;
        default:
            cout<<"Enter valid Operation."<<endl;
        }

    }while(operation!=0);

    return 0;
}
