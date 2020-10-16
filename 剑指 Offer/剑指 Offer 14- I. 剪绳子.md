# 剑指 Offer 14- I. 剪绳子

给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：
```
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
```
示例 2:
```
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
```
提示：
+ 2 <= n <= 58

注意：本题与主站 343 题相同：https://leetcode-cn.com/problems/integer-break/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
算术几何均值不等式可得，当所有绳段长度相等时，乘积最大  
令 n=ax 有 最大结果为 x^a = x^(n/x) = [x^(1/x)]^n  
也就是 x^(1/x) 最大为e时，结果最大，取整后3优于2  
所以，每段尽可能取3。最后剩下2时可不管，剩下1时把一个3拆为2*2  
详细推导见[此处](https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/mian-shi-ti-14-i-jian-sheng-zi-tan-xin-si-xiang-by/)  
同时用快速幂加速  
``` java
class Solution {
    public int cuttingRope(int n) {
        if (n < 0)
            return 0;
        if (n <= 2)
            return 1;
        if (n == 3)
            return 2;
        int remain = n % 3;
        int m = n / 3;
        if (remain == 2) {
            return 2 * quickPow(3, m);
        } else if (remain == 1) {
            m -= 1;
            return 4 * quickPow(3, m);
        } else if (remain == 0) {
            return quickPow(3, m);
        }
        return 0;
    }

    private int quickPow(int base, int exponent) {
        if (exponent == 0) {
            return 1;
        }
        int halfExponent = exponent / 2;
        boolean odd = exponent % 2 == 1;
        int result = quickPow(base, halfExponent);
        if (odd)
            return result * result * base;
        else
            return result * result;
    }
}
```