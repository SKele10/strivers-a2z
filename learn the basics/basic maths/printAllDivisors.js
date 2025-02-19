// User function Template for javascript
/**
 * @param {number} n
 * @returns {number}
 */

class Solution {
  // Function to find sum of divisors
  sumOfDivisors(n) {
    let sum = 0;
    for (let i = 1; i <= n; i++) {
      for (let j = 1; j <= i; j++) {
        if (i % j === 0) sum += j;
      }
    }
    return sum
  }
}

const solution = new Solution();
console.log(solution.sumOfDivisors(1))
