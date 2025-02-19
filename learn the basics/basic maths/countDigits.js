class Solution {
    // Function to check whether the number evenly divides n.
    evenlyDivides(n) {
      let count = 0;
      const text = n.toString();
      text.split('').forEach((d) => {
        const digit = Number.parseInt(d);
        if (n % digit === 0) count++;
      });
      return count;
    }
  }
  
  const solution = new Solution();
  console.log(solution.evenlyDivides(12));
  