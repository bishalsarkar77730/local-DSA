public class Maximum_Subarray_Sum_calude {

    public static int maximumSum(int[] nums) {
        // Integer.MIN_VALUE is the Java equivalent to float("-inf") for integers
        int maxSum = Integer.MIN_VALUE;

        // Handle empty array edge case
        if (nums == null || nums.length == 0) {
            return 0;
        }

        for (int i = 0; i < nums.length; i++) { // i = start of the chunk
            int currentSum = 0; // reset the running total for each new start

            for (int j = i; j < nums.length; j++) { // j = end of the chunk, starts AT i
                currentSum += nums[j]; // extend the chunk by one element, add its value

                if (currentSum > maxSum) {
                    maxSum = currentSum;
                }
            }
        }

        System.out.println(maxSum);
        return maxSum;
    }

    public static void main(String[] args) {
        // Example usage
        int[] nums = { 1, 2, 3, -2, 5 };
        maximumSum(nums);
    }
}