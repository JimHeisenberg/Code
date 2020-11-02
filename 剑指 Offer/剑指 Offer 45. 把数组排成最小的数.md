# 剑指 Offer 45. 把数组排成最小的数

输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

示例 1:
```
输入: [10,2]
输出: "102"
```
示例 2:
```
输入: [3,30,34,5,9]
输出: "3033459"
```
提示:
+ 0 < nums.length <= 100

说明:
+ 输出结果可能非常大，所以你需要返回一个字符串而不是整数
+ 拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
如果 ab < ba 则最终结果中a应该在b之前  
快速排序  
可以用数学归纳法证明  
``` java
class Solution {
    public String minNumber(int[] nums) {
        for (int num : nums) {
            if (num < 0)
                throw new RuntimeException();
        }
        quickSort(nums, 0, nums.length - 1);
        StringBuilder buffer = new StringBuilder();
        for (int num : nums)
            buffer.append(String.valueOf(num));
        return buffer.toString();
    }

    private void quickSort(int[] arr, int start, int end) {
        if (start >= end)
            return;
        int l = start;
        int r = end;
        int temp = arr[l];
        while (l < r) {
            while (l < r && cmp(temp, arr[r]))
                r--;
            arr[l] = arr[r];
            while (l < r && cmp(arr[l], temp))
                l++;
            arr[r] = arr[l];
        }
        arr[l] = temp;
        quickSort(arr, start, l - 1);
        quickSort(arr, l + 1, end);
        return;
    }

    private boolean cmp(int a, int b) {
        // return ab <= ba;
        String aString = Integer.toString(a);
        String bString = Integer.toString(b);
        StringBuilder ab = new StringBuilder(aString);
        StringBuilder ba = new StringBuilder(bString);
        ab.append(bString);
        ba.append(aString);
        return (ab.compareTo(ba) <= 0);
    }
}
```