# 剑指 Offer 40. 最小的k个数

输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例 1：
```
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
```
示例 2：
```
输入：arr = [0,1,2,1], k = 1
输出：[0]
```
限制：
+ 0 <= k <= arr.length <= 10000
+ 0 <= arr[i] <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
快速排序后返回前k个元素  
``` java
class Solution {
    public int[] getLeastNumbers(int[] arr, int k) {
        quickSort(arr, 0, arr.length - 1);
        if (k > arr.length)
            // or throw new IndexOutOfBoundsException();
            return arr;
        int[] result = new int[k];
        for (int i = 0; i < result.length; i++)
            result[i] = arr[i];
        return result;
    }

    private void quickSort(int[] arr, int start, int end) {
        if (start >= end)
            return;
        int l = start;
        int r = end;
        int temp = arr[l];
        while (l < r) {
            while (l < r && arr[r] >= temp)
                r--;
            arr[l] = arr[r];
            while (l < r && arr[l] <= temp)
                l++;
            arr[r] = arr[l];
        }
        arr[l] = temp;
        quickSort(arr, start, l - 1);
        quickSort(arr, l + 1, end);
        return;
    }
}
```