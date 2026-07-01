const num = [2, 7, 11, 15];
const target = 9;

function twosum2() {
  let left = 0;
  let right = num.length - 1;
  while (left < right) {
    const sum = num[left] + num[right];
    if (sum === target) {
      console.log([left + 1, right + 1]);
      return [left + 1, right + 1];
    } else if (sum < target) {
      left += 1;
    } else {
      right -= 1;
    }
  }
  console.log([]);
  return [];
}

twosum2();
