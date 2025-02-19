
/**
 * @param {number} n
 * @returns { }
 */
let number = 1
class Solution {
    printNos(n) {
        if (n === 0) return;

        this.printNos(n - 1);
        console.log(n + " ");;
    }
}


const solution = new Solution();
solution.printNos(64);