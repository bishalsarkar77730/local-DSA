const s = "aba";

function is_palindrome_range(s, i, j) {
  while (i < j) {
    if (s[i] != s[j]) {
      return false;
    }
    i += 1;
    j -= 1;
  }
  return true;
}

const valid_palindrome = (s) => {
  let left = 0;
  let right = s.length - 1;
  while (left < right) {
    if (s[left] === s[right]) {
      left += 1;
      right -= 1;
    } else {
      let skip_left = is_palindrome_range(s, left + 1, right);
      let skip_right = is_palindrome_range(s, left, right - 1);
      return skip_left || skip_right;
    }
  }
  return True;
};
