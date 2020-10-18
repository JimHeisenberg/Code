# 剑指 Offer 16. 数值的整数次方

实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

示例 1:
```
输入: 2.00000, 10
输出: 1024.00000
```
示例 2:
```
输入: 2.10000, 3
输出: 9.26100
```
示例 3:
```
输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
```
说明:
+ -100.0 < x < 100.0
+ n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。

注意：本题与主站 50 题相同：https://leetcode-cn.com/problems/powx-n/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
快速幂  
``` java
class Solution {
    public double myPow(double x, int n) throws RuntimeException {
        double base = x;
        long exponent = n;
        if (n < 0) {
            if (x == 0 && n != 0)
                throw new RuntimeException();
            base = 1 / base;
            exponent = -exponent;
        }
        return quickPow(base, exponent);
    }

    private double quickPow(double base, long positiveExponent) {
        if (positiveExponent == 0) {
            // note 0⁰ is regarded as 1
            return 1;
        }
        long halfExponent = positiveExponent >> 1;
        boolean odd = (positiveExponent & 1) == 1;
        double result = quickPow(base, halfExponent);
        if (odd)
            result = result * result * base;
        else
            result = result * result;
        return result;
    }
}
```