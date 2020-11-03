# 剑指 Offer 56 - II. 数组中数字出现的次数 II

在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

示例 1：
```
输入：nums = [3,4,3,3]
输出：4
```
示例 2：
```
输入：nums = [9,1,7,9,7,9,7]
输出：1
```
限制：
+ 1 <= nums.length <= 10000
+ 1 <= nums[i] < 2^31

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
位运算，统计每一位上出现的1的次数，如果不是3的倍数，则说明是只出现一次的数字贡献的  
``` java
class Solution {
    public int singleNumber(int[] nums) {
        // countBit(5) -> {1, 0, 1, 0, 0, 0, 0, 0, ... }
        int[] bitCountArray = new int[Integer.SIZE];
        for (int num : nums)
            countBit(num, bitCountArray);
        int result = 0, bit = 1;
        for (int bitCount : bitCountArray) {
            if (bitCount % 3 == 1)
                result += bit;
            bit <<= 1;
        }
        return result;
    }

    private void countBit(int num, int[] bitCountArray) {
        int bit = 1;
        for (int i = 0; i < Integer.SIZE; i++) {
            if ((num & bit) == bit)
                bitCountArray[i]++;
            bit <<= 1;
        }
    }
}
```