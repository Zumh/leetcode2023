#include <stdio.h>
#include <stdbool.h>
#include <iostream>

class Solution {
	public: 
		Solution();

		bool isPalindrome(int x);
		~Solution();
};

Solution::Solution(){};
Solution::~Solution(void){}

bool Solution::isPalindrome(int x)
{
	if (x < 0)
	{
		return false;
	}

	int digits = 0;
	int reverse = 0;
	int original = x;

	// reverse the number here 
	while(x > 0)
	{
		digits = x % 10;

		reverse = reverse * 10 + digits;

		x = x/10;
	}
	return original == reverse;
}

int main(void)
{

	Solution palindrome;
	
	bool status = palindrome.isPalindrome(121);
	printf("%d\n", status);

	return 0;
}
