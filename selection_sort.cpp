int select(int arr[], int i)
{
    return arr[i];
    // code here such that selecionSort() sorts arr[]
}


void selectionSort(int arr[], int n)
{
  //code here
  int min_index;
  
  for(int i=0;i<=n-2;i++)
  {  int temp=0;
      
      
      min_index=i;
      for(int j=i+1;j<=n-1;j++)
      {
          if(arr[j]<arr[min_index])
          min_index=j;
      }
      if(min_index != i)
      {temp=arr[i];
       arr[i]=arr[min_index];
       arr[min_index]=temp;
       
      }
      select(arr,i);
      
  }
  
}   
