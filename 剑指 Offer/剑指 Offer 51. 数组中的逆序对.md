# 剑指 Offer 51. 数组中的逆序对

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

示例 1:
```
输入: [7,5,6,4]
输出: 5
```

限制：
+ 0 <= 数组长度 <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
依次比较 时间复杂度O(n²) 空间复杂度O(1)  
***会超出时间限制***
``` java
class Solution {
    public int reversePairs(int[] nums) {
        int result = 0;
        for (int i = 0; i < nums.length; i++)
            for (int j = i + 1; j < nums.length; j++)
                if (nums[i] > nums[j])
                    result++;
        return result;
    }
}
```

# Solution 2
归并算法 时间复杂度O(nlogn) 空间复杂度O(n)  
``` java
class Solution {
    private int count;

    public int reversePairs(int[] nums) {
        if (nums.length == 0)
            return 0;
        count = 0;
        mergeSortAndCount(nums, 0, nums.length - 1);
        return count;
    }

    private int[] mergeSortAndCount(int[] nums, int l, int r) {
        if (l == r)
            return new int[] { nums[l] };
        int mid = l + (r - l) / 2;
        int[] leftArr = mergeSortAndCount(nums, l, mid);
        int[] rightArr = mergeSortAndCount(nums, mid + 1, r);
        int[] newNum = new int[leftArr.length + rightArr.length];
        int m = 0, i = 0, j = 0;
        while (i < leftArr.length && j < rightArr.length) {
            if (leftArr[i] <= rightArr[j])
                newNum[m++] = leftArr[i++];
            else {
                newNum[m++] = rightArr[j++];
                // 将rightArr中的一个元素放在了(leftArr.length-i)个比它大的元素之前
                count += leftArr.length - i;
            }
        }
        while (i < leftArr.length)
            newNum[m++] = leftArr[i++];
        while (j < rightArr.length)
            newNum[m++] = rightArr[j++];
        return newNum;
    }
}
```

# Solution 3
利用二叉排序树(每个节点统计子节点数量)  
先将n个元素插入二叉排序树{ O(nlogn) }  
然后对每个元素统计二叉排序树中小于自己的数字的数量{ O(nlogn) }  
最后删除自身{ O(nlogn) }  
应该是可行的，但过于复杂  
