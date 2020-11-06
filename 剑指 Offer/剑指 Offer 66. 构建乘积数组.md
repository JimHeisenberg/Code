# 剑指 Offer 66. 构建乘积数组

给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

示例:
```
输入: [1,2,3,4,5]
输出: [120,60,40,30,24]
```

提示：
+ 所有元素乘积之和不会溢出 32 位整数
+ a.length <= 100000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
空间换时间，记录从左和从右开始的连乘结果  
``` java
class Solution {
    public int[] constructArr(int[] a) {
        if (a.length == 0)
            return new int[0];
        int[] leftMultiplyArray = new int[a.length];
        leftMultiplyArray[0] = 1;
        for (int i = 1; i < leftMultiplyArray.length; i++)
            leftMultiplyArray[i] = leftMultiplyArray[i - 1] * a[i - 1];
        int[] rightMultiplyArray = new int[a.length];
        rightMultiplyArray[rightMultiplyArray.length - 1] = 1;
        for (int i = rightMultiplyArray.length - 2; i >= 0; i--)
            rightMultiplyArray[i] = rightMultiplyArray[i + 1] * a[i + 1];
        int[] result = new int[a.length];
        for (int i = 0; i < result.length; i++)
            result[i] = leftMultiplyArray[i] * rightMultiplyArray[i];
        return result;
    }
}
```
