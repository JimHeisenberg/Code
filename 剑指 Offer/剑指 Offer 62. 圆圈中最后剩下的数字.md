# 剑指 Offer 62. 圆圈中最后剩下的数字

0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

示例 1：
```
输入: n = 5, m = 3
输出: 3
```
示例 2：
```
输入: n = 10, m = 17
输出: 2
```
限制：
+ 1 <= n <= 10^5
+ 1 <= m <= 10^6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
递归解法  
``` java
class Solution {
    public int lastRemaining(int n, int m) {
        // suppose the first deleted number is k-1 = kth = m % n
        // the circle can be formed as [0, 1, ... k-2, /k-1/, k, ... n-1]
        // the next number to delete starts from k, and it is the mth number
        // so circle can be reformed as [k, ... n-1, 0, 1, ... k-2], length = n-1
        // then use wishful thinking, suppose we've known x = lastRemaining(n-1, m)
        // which means in [0, 1, ... n-2] lastRemaining(n-1, m) is x
        // then remap x from [0, 1, ... n-2] into [k, ... n-1, 0, 1, ... k-2]
        // that is if (x < n - k) x += k; else x -= n - k;
        if (n == 0)
            return 0;
        int x = lastRemaining(n - 1, m);
        int k = m % n;
        if (x < n - k)
            x += k;
        else
            x -= n - k;
        return x;
    }
}
```

# Solution 1
循环解法  
``` java
class Solution {
    public int lastRemaining(int n, int m) {
        // suppose the first deleted number is k-1 = kth = m % n
        // the circle can be formed as [0, 1, ... k-2, /k-1/, k, ... n-1]
        // the next number to delete starts from k, and it is the mth number
        // so circle can be reformed as [k, ... n-1, 0, 1, ... k-2], length = n-1
        // then use wishful thinking, suppose we've known x = lastRemaining(n-1, m)
        // which means in [0, 1, ... n-2] lastRemaining(n-1, m) is x
        // then remap x from [0, 1, ... n-2] into [k, ... n-1, 0, 1, ... k-2]
        // that is if (x < n - k) x += k; else x -= n - k;
        // we can rename the n above into i, and use loop instead of recursion
        // this process is repeated from i = 1 to i = n
        int x = 0;
        for (int i = 1; i <= n; i++) {
            int k = m % i;
            if (x < i - k)
                x += k;
            else
                x -= i - k;
        }
        return x;
    }
}
```
