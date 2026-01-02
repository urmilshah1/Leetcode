int heightChecker(int* a,int n){
    int e[n],c=0,t,i,j;
    for(i=0;i<n;i++)
    e[i]=a[i];
    for(i=0;i<n-1;i++)
        for(j=0;j<n-i-1;j++)
            if(a[j]>a[j+1])
            {
                t=a[j];
                a[j]=a[j+1];
                a[j+1]=t;
            }
    for(i=0;i<n;i++)
        if(e[i]!=a[i])
        c++;
    return c;
}
