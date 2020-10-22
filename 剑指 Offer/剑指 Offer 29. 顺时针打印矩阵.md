# 剑指 Offer 29. 顺时针打印矩阵

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

示例 1：
```
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
```
示例 2：
```
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
```
限制：
+ 0 <= matrix.length <= 100
+ 0 <= matrix[i].length <= 100

注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
按圈依次遍历  
``` java
class Solution {
    public int[] spiralOrder(int[][] matrix) {
        if (matrix.length == 0)
            return new int[0];
        int rowLen = matrix.length;
        int colLen = matrix[0].length;
        int rank = rowLen < colLen ? (rowLen + 1) / 2 : (colLen + 1) / 2;
        boolean lastHalfCircle = rowLen < colLen ? rowLen % 2 == 1 : colLen % 2 == 1;
        int[] result = new int[rowLen * colLen];
        int count = 0;
        for (int n = 0; n < rank; n++) {
            for (int i = n; i < colLen - n; i++)
                result[count++] = matrix[n][i];
            for (int i = n + 1; i < rowLen - n; i++)
                result[count++] = matrix[i][colLen - n - 1];
            if (n == rank - 1 && lastHalfCircle)
                break;
            for (int i = colLen - n - 2; i >= n; i--)
                result[count++] = matrix[rowLen - n - 1][i];
            for (int i = rowLen - n - 2; i > n; i--)
                result[count++] = matrix[i][n];
        }
        return result;
    }
}
```