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

# Summary
因为不同的功能/性能要求，以及题目本身带有的特点不同，所以  
***写代码之前先考虑清楚需求***

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

# Solution 2
题目的变体  
长度为n+1的数组里的所有数字在1~n的范围内，不修改数组找出重复数字  
*注意，因为这里数字的范围是1~n，不包括0，所以必然在某个数字的区间中会多出一个数，所以才能使用二分查找*
``` java
class Solution {
    public int findRepeatNumber(int[] nums) {
        // 不修改数组，将取值范围按照二分法划分
        // 如果一个范围内的数字出现次数大于范围长度
        // 则这个范围内存在重复数字
        // 要求nums中的区间必然多出一个数字
        // 比如[2,2,3,4]不能用这个算法，因为不满足
        // 长度为n+1的数组里的所有数字在1~n的范围内
        int start = 1;
        int end = nums.length - 1;
        int mid = 1;
        while (start < end) {
            mid = (start + end) / 2;
            if (checkHalf(nums, start, mid)) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        return start;
    }

    private boolean checkHalf(int[] nums, int start, int end) {
        int count = 0;
        for (int i : nums) {
            if (start <= i && i <= end) {
                count++;
            }
        }
        if (count > end - start + 1) {
            return true;
        }
        return false;
    }

    public static void main(String[] args) {
        int[] nums = { 1, 2, 3, 3, 4 };
        Solution s = new Solution();
        int x = s.findRepeatNumber(nums);
        System.out.println(x);
    }
}
```