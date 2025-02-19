/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
  const reverse = +Math.abs(x).toString().split("").reverse().join("");

  if (reverse > 0x7fffffff) {
    return 0;
  }
  return reverse * Math.sign(x);
};

console.log(reverse(-5896));
