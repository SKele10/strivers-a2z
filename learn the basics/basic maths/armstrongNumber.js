/**
 * @param {number} n
 * @returns {boolean}
 */

class Solution {
    armstrongNumber(n) {
        const numberArray = n.toString().split("")
        let sum = 0
        numberArray.forEach(d => {
            sum += d**numberArray.length
        });
        return n === sum
    }
}

const solution = new Solution()
console.log(solution.armstrongNumber(372))