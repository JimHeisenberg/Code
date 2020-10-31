# 剑指 Offer 43. 1～n 整数中 1 出现的次数

输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。

例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。

示例 1：
```
输入：n = 12
输出：5
```
示例 2：
```
输入：n = 13
输出：6
```
限制：
+ 1 <= n < 2^31

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
分别计算n中每一位出现1的数量，bitPos表示当前位  
``` java
class Solution {
    public int countDigitOne(int n) {
        if (n <= 0)
            return 0;
        long count = 0;
        long bitPos = 1;
        while (bitPos <= n) {
            long low = 0;
            if (bitPos != 1)
                low = n % bitPos;
            long cur = n / bitPos % 10;
            long high = n / bitPos / 10;
            long bitCount = 0;
            if (cur == 0)
                bitCount = high * bitPos;
            else if (cur == 1)
                bitCount = high * bitPos + low + 1;
            else
                bitCount = (high + 1) * bitPos;
            count += bitCount;
            bitPos *= 10;
        }
        return (int) count;
    }
}
```