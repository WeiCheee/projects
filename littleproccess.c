

for(i=0; i<n; i++){
    if(list[i]<=90 && list[i]>=65){
        list[i]+=32;
    }else if (list[i]<=122 && list[i]>=97)
    {
        list[i]-=32;
    }else
    {
        print("not a word")
    }
}

int isPowerof2(int n){
    return n>0 && (n&(n-1) == 0)
}
int isPowerof2(int n){
    for(i=0; i<n; i*=2){
        if(i == n){
            return 1;
        }else{
            return 0;
        }
    }
}

ans = ans<<1 | (n&1)
n/=2

while(n){
    count++;
    n&=(n-1);
}
