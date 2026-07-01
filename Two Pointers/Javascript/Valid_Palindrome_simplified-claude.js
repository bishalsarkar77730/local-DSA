const s = "racecar";

function is_palindrom() {
  let left = 0;
  let right = s.length - 1;
  while (left < right) {
    if (s[left] != s[right]) {
      console.log("false");
      return false;
    }
    left += 1;
    right -= 1;
  }
  console.log("true");
  return true;
}

is_palindrom()