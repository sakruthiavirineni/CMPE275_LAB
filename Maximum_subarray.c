
#include<limits.h>
#include<stdio.h>
#include<stdlib.h>
int maxSubArraySum(int* nums, int numsSize){
    int best_value = INT_MIN;
    int total_sum = 0;
    for (int i=0; i<numsSize; i++)
    {

        if(total_sum+nums[i]>nums[i]){
            total_sum=total_sum+nums[i];
        }
        else{
            total_sum=nums[i];
        }
        if(total_sum>best_value){
            best_value=total_sum;
        }
    }

    return best_value;
}