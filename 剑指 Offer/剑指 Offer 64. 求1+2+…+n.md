# 剑指 Offer 64. 求1+2+…+n

求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

示例 1：
```
输入: n = 3
输出: 6
```
示例 2：
```
输入: n = 9
输出: 45
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/qiu-12n-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
利用 && || 的短路特性，左边判断递归是否结束，右边对n赋值  
``` java
class Solution {
    public int sumNums(int n) {
        boolean endLoop = (n != 0 && (n += sumNums(n - 1)) > 0);
        return n;
    }
}
```
``` java
class Solution {
    public int sumNums(int n) {
        boolean endLoop = (n == 0 || (n += sumNums(n - 1)) > 0);
        return n;
    }
}
```