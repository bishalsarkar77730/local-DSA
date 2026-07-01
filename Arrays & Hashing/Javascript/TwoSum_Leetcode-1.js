const nums = [2, 7, 11, 15];
const target = 9;

// bruteforce
function twosum(nums) {
  for (let num = 0; num < nums.length; num++) {
    for (let i = num + 1; i < nums.length; i++) {
      if (nums[num] + nums[i] === target) console.log([num, i]);
      return;
    }
  }
}

// twosum(nums);

// Hashmap

function twosumhash(nums) {
  const seen = new Map();
  for (let i = 0; i < nums.length; i++) {
    let complement = target - nums[i];
    if (seen.has(complement)) {
      console.log([seen.get(complement), i]);
      return;
    }
    seen.set(nums[i], i);
  }
  return [];
}
twosumhash(nums);
