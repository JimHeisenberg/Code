# 剑指 Offer 10- II. 青蛙跳台阶问题

一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：
```
输入：n = 2
输出：2
```
示例 2：
```
输入：n = 7
输出：21
```
示例 3：
```
输入：n = 0
输出：1
```
提示：
+ 0 <= n <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
所求为斐波那契数列的第n+1项  
``` java
class Solution {
    public int numWays(int n) {
        // a=f(n), b=f(n+1), c=f(n+2)
        int a = 0;
        int b = 1;
        int c = 1;
        for (int i = 0; i <= n; i++) {
            a = b;
            b = c;
            c = a + b;
            if (c > 1e9 + 7)
                c -= 1e9 + 7;
        }
        return a;
    }
}
```