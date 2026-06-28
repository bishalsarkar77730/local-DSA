const nums = [-3, -1, -2]
const maximum_sum = () =>{
    let maxVal = Number.NEGATIVE_INFINITY;
    for (let i = 0; i < nums.length; i++ ){
        let current_sum = 0
        for (let j = i; j < nums.length; j++) {
            current_sum += nums[j];
            if (current_sum > maxVal) {
                maxVal = current_sum;
            }
        }
    }
    console.log(maxVal);
    return maxVal;
}

maximum_sum();