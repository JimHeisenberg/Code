# 剑指 Offer 03. 数组中重复的数字

找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：
```
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 
```
限制：
+ 2 <= n <= 100000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
利用 *长度为 n 的数组 nums 里的所有数字都在 0～n-1* 这一特点, 原地置换数组, 使nums[i]=i, 过程中可发现重复  
``` java
class Solution {
    public int findRepeatNumber(int[] nums) {
        // Because number in nums are in range 0 ~ n-1
        // we can put i to nums[i], and conflict means repeated
        int temp = 0;
        for (int i = 0; i < nums.length; i++) {
            while (nums[i] != i) {
                temp = nums[i];
                if (nums[temp] == temp) {
                    return temp;
                }
                nums[i] = nums[temp];
                nums[temp] = temp;
            }
        }
        return -1;
    }
}
```