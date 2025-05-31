#include <stdio.h>
#include <vector>
#include <iostream>
#include <map>

using namespace std;
vector<int> twoSum(vector<int>& nums, int target){
	int numberInArray = 0;
	int difference = 0;
	int currentDifference = 0;
	vector<int> result;
	map<int, int> differences;
	for(size_t index = 0; index < nums.size(); index++)
	{
		int currentNumber = nums[index];

		int currentDifference = target - currentNumber;

		if (differences.count(currentDifference) > 0)
		{
			// store answer
			result.push_back( differences[ currentDifference ] );
			result.push_back( index );
			return result; 
		}

		// insert unique value and index
		differences[ currentNumber ] =  index;
	}


	    
	return {0, 0};
}

int main(void)
{
	vector<int> nums = {2,7,11,15};
	vector<int> result = twoSum(nums, 9);
	for(size_t index = 0; index < result.size(); index++)
	{
		printf("%d \n", result[index]);
	}
	return 0;
}
    
