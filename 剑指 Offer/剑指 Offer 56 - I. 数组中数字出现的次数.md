# 剑指 Offer 56 - I. 数组中数字出现的次数

一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

示例 1：
```
输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
```
示例 2：
```
输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]
```
限制：
+ 2 <= nums.length <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
利用 N xor N == 0 这一特点  
如果是 *nums 里除1个数字之外，其他数字都出现了两次* ，一次xor可得结果  
但因为有2不同数字，所以假设它们是[a,b]，则xor全部数组可得 a xor b ，记为xorResult  
xorResult 中一定有为1的比特，可以利用这个比特把nums分为两个部分，每个部分中只有一个不重复数字  
``` java
class Solution {
    public int[] singleNumbers(int[] nums) {
        // suppose nums = {a, b, c, c, d, d, e, e, ... }
        int[] result = { 0, 0 };
        // xorResult == a xor b
        int xorResult = 0;
        for (int num : nums)
            xorResult ^= num;
        // differentBit = the first different bit of [a,b] from right to left
        int differentBit = 1;
        while ((xorResult & differentBit) == 0)
            differentBit <<= 1;
        // group nums by differentBit and xor again to find [a,b]
        for (int num : nums) {
            if ((num & differentBit) == 0)
                result[0] ^= num;
            else
                result[1] ^= num;
        }
        return result;
    }
}
```