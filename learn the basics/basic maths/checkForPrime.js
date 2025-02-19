// User function Template for javascript

/**
 * @param {number} n
 * @return {number}
 */

class Solution {
  isPrime(n) {
    let count = 0;
    for (let i = 1; i <= n; i++) {
        if (n % i === 0) count++;
        if (count > 2) return false;
    }
    return count === 2;
  }
}

const solution = new Solution();
console.log(solution.isPrime(9));
