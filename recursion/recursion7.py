https://www.codechef.com/problems/CHEFMATH
Chef's team is going to participate at the legendary math battles. One of the main task in the competition is to calculate the number of ways to create a number by adding some Chefonacci numbers. A number is called a Chefonacci number if it is an element of Chefonacci sequence defined as follows.


f(0) = 1; 
f(1) = 2; 
For i > 1 : f(i) = f(i - 1) + f(i - 2)

Chef asked you to help him with this task. There will be Q question of form X, K : How many different ways are there to create X by adding K Chefonacci numbers. Note that the order of numbers in the addition does not matter, i.e. (f(i) + f(j) + f(k)) and (f(j) + f(i) + f(k)) will not be counted as distinct ways. Also note that you are allowed to use a Chefonacci number any number of times (zero or more).

As the answer could be large, print your answer modulo 109 + 7 (1000000007).


#include<stdio.h>
 
#define MOD 1000000007
 
int count;
 
void calc(int chef[], int n, int sum, int index)
{
	//printf("n=%d sum=%d index=%d count=%d\n",n,sum,index,count);
	if(index<0)
		return;
	if(sum<0)
		return;
	if((long long)chef[index]*n < sum)
		return;
	if(n==0)
	{
		if(sum==0)
			count=(count+1)%MOD;
		return;
	}
	calc(chef,n-1,sum-chef[index],index);
	calc(chef,n,sum,index-1);	
}
 
int main()
{
	int i, q, x, k;
	int chef[43];
	chef[0]=1;
	chef[1]=2;
	for(i=2;i<43;i++)
		chef[i]=chef[i-1]+chef[i-2];
	scanf("%d",&q);
	while(q--)
	{
		count=0;
		scanf("%d%d",&x,&k);
		calc(chef,k,x,42);
		printf("%d\n",count);
	}
	return 0;
} 
