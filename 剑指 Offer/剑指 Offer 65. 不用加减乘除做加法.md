# 剑指 Offer 65. 不用加减乘除做加法

写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

示例:
```
输入: a = 1, b = 1
输出: 2
```

提示：
+ a, b 均可能是负数或 0
+ 结果不会溢出 32 位整数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
利用二进制做运算  
a+b可以分解为不进位相加(a xor b)和加上进位(a&b << 1)  
加法的结果也可能产生进位，所以把新的加法再次分解，直到进位为0  
``` java
class Solution {
    public int add(int a, int b) {
        int result = a ^ b;
        int carry = (a & b) << 1;
        while (carry != 0) {
            a = result;
            b = carry;
            result = a ^ b;
            carry = (a & b) << 1;
        }
        return result;
    }
}
```