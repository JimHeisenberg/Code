# 剑指 Offer 46. 把数字翻译成字符串

给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

示例 1:
```
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
```

提示：
+ 0 <= num < 2^31

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
从右向左递推  
``` java
class Solution {
    public int translateNum(int num) {
        if (num < 0)
            return 0;
        int currentCount = 1;
        int currentlBit = 0;
        int lastCount = 0;
        int lastTwoCount = 0;
        int lastBit = 0;
        while (num != 0) {
            lastTwoCount = lastCount;
            lastCount = currentCount;
            lastBit = currentlBit;
            currentlBit = num % 10;
            num /= 10;
            // if (10 <= currentlBit * 10 + lastBit <= 25)
            if (currentlBit == 1 || (currentlBit == 2 && lastBit <= 5))
                currentCount = lastCount + lastTwoCount;
            else
                currentCount = lastCount;
        }
        return currentCount;
    }
}
```