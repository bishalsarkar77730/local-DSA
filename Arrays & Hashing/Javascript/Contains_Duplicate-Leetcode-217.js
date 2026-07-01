const arr = [1, 2, 3, 4];

function findDuplicateHashmap() {
  let seen = new Map();
  for (let i = 0; i < arr.length; i++) {
    if (seen.has(arr[i])) {
      console.log("True");
      return true;
    }
    seen.set(arr[i]);
  }
  console.log("False");
  return false;
}

findDuplicateHashmap()