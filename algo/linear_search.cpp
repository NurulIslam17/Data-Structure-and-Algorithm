#include<iostream>
using namespace std;
int main()
{
    int n,i,searchEle,arr[100];
    cin>>n;
    cin>>searchEle;
    bool isFound = false;
    for(int i=0; i<n; i++)
    {
        cin>>arr[i];
    }
    for(i=0; i<n; i++)
    {
        if(searchEle==arr[i])
        {
            isFound=true;
            break;
        }
    }
    if(isFound)
    {
        cout<<searchEle<<" is found at pos["<<i<<"]"<<endl;
    }
    else
    {
        cout<<searchEle<<" is not found"<<endl;
    }

    return 0;
}
