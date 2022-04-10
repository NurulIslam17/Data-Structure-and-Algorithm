#include<bits/stdc++.h>
#include<iostream>
using namespace std;

int binarySearch(int arr[], int n, int searchItem)
{
    int s =0;
    int e = n;
    while(s<=e)
    {
        int mid =(s+e)/2;
        if(arr[mid]==searchItem)
        {
           return mid;
        }
        else if (arr[mid]>searchItem)
        {
            e=mid-1;
        }
        else
        {
            s=mid+1;
        }
    }
    return -1;
}

int main()
{
    int n,searchItem;
    cin>>n;
    int arr[n];
    for(int i=0; i<n; i++)
    {
        cin>>arr[i];
    }
    cin>>searchItem;
    cout<<binarySearch(arr,n,searchItem)<<endl;

    return 0;
}
