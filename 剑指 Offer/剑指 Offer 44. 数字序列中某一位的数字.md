# 剑指 Offer 44. 数字序列中某一位的数字

数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数，求任意第n位对应的数字。

示例 1：
```
输入：n = 3
输出：3
```
示例 2：
```
输入：n = 11
输出：0
```
限制：
+ 0 <= n < 2^31

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
result = numBitCount / 9 + numBitOffset; 表示n所在数字的具体值  
numBitLen 表示result的位长度, numBitLen=2 -> result是2位数  
numBitCount 表示位数与result相同的数的数量, numBitCount=90 -> 2位数有90个  
numBitOffset 表示result是numBitLen位数中的第几个(numBitOffset=0对应1后全0), numBitOffset=0 -> result是第1个2位数(10)  
numBitPosition 表示n是result中的第几位(最右边为第0位), numBitPosition=1 -> n是result(10)的第1位1  
``` java
class Solution {
    public int findNthDigit(int n) {
        if (n <= 0)
            return 0;
        if (n <= 9)
            return n;
        long numBitLen = 1;
        long numBitCount = 9;
        long numBitOffset = 0;
        long numBitPosition = 0;
        while (n > numBitCount * numBitLen) {
            n -= numBitCount * numBitLen;
            numBitLen++;
            numBitCount *= 10;
        }
        n--;
        numBitOffset = n / numBitLen;
        numBitPosition = numBitLen - (n % numBitLen);
        long result = numBitCount / 9 + numBitOffset;
        while (--numBitPosition > 0)
            result /= 10;
        result %= 10;
        return (int) result;
    }
}
```