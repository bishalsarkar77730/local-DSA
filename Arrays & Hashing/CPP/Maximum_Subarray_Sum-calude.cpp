#include <iostream>
#include <vector>
#include <limits>

int maximum_sum(const std::vector<int>& nums) {
    // negative infinity — handles the all-negatives trap
    // std::numeric_limits<int>::lowest() is the C++ equivalent to float("-inf") for integers
    int max_sum = std::numeric_limits<int>::lowest(); 

    // Handle empty array edge case to prevent errors
    if (nums.empty()) return 0;

    for (size_t i = 0; i < nums.size(); ++i) {  // i = start of the chunk
        int current_sum = 0;  // reset the running total for each new start
        
        for (size_t j = i; j < nums.size(); ++j) {  // j = end of the chunk, starts AT i
            current_sum += nums[j];  // extend the chunk by one element, add its value
            
            if (current_sum > max_sum) {
                max_sum = current_sum;
            }
        }
    }
    
    std::cout << max_sum << std::endl;
    return max_sum;
}

int main() {
    // Example usage
    std::vector<int> nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    maximum_sum(nums);
    
    return 0;
}