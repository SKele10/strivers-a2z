class Solution {
  /**
    * @param number a
    * @param number b

    * @returns number[]
    */
  lcmAndGcd(a, b) {
    const min = Math.min(a, b)
    const divisors = new Set();
    let gcd = 1;
    for (let i = 1; i <= min; i++) {
      if (a % i == 0 && b % i == 0) {
        gcd = i
        divisors.add(i);
      }
    }
    const lcm = (a * b) / gcd;
    return [lcm, gcd];
  }
}

let solution = new Solution();
console.log(solution.lcmAndGcd(10, 5));
