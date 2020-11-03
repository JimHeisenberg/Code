# 剑指 Offer 53 - I. 在排序数组中查找数字 I

统计一个数字在排序数组中出现的次数。

示例 1:
```
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
```
示例 2:
```
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
```
限制：
+ 0 <= 数组长度 <= 50000

注意：本题与主站 34 题相同（仅返回值不同）：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
两次二分查找  
``` java
class Solution {
    public int search(int[] nums, int target) {
        int firstIndex = binarySearchFirst(target, nums, 0, nums.length - 1);
        if (firstIndex == -1)
            return 0;
        int lastIndex = binarySearchLast(target, nums, 0, nums.length - 1);
        return lastIndex - firstIndex + 1;
    }

    private int binarySearchFirst(int target, int[] nums, int start, int end) {
        int mid = 0;
        while (start <= end) {
            mid = (start + end) / 2;
            if (nums[mid] == target && (mid == 0 || nums[mid - 1] < target))
                return mid;
            else if (nums[mid] < target)
                start = mid + 1;
            else
                end = mid - 1;
        }
        return -1;
    }

    private int binarySearchLast(int target, int[] nums, int start, int end) {
        int mid = 0;
        while (start <= end) {
            mid = (start + end) / 2;
            if (nums[mid] == target && (mid == nums.length - 1 || nums[mid + 1] > target))
                return mid;
            else if (nums[mid] <= target)
                start = mid + 1;
            else
                end = mid - 1;
        }
        return -1;
    }
}
```