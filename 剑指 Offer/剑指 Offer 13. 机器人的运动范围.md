# 剑指 Offer 13. 机器人的运动范围

地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：
```
输入：m = 2, n = 3, k = 1
输出：3
```
示例 2：
```
输入：m = 3, n = 1, k = 0
输出：1
```
提示：
+ 1 <= n,m <= 100
+ 0 <= k <= 20

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
递归查找，记录每一格是否被访问过  
``` java
class Solution {

    public int movingCount(int m, int n, int k) {
        if (m <= 0 || n <= 0 || k < 0)
            return 0;
        boolean[][] visitedMat = new boolean[m][n];
        // for (int i = 0; i < visitedMat.length; i++) {
        // for (int j = 0; j < visitedMat[0].length; j++) {
        // visitedMat[i][j] = false; } }
        return recursiveCount(visitedMat, 0, 0, k);
    }

    private int recursiveCount(boolean[][] visitedMat, int i, int j, int k) {
        if (i < 0 || i >= visitedMat.length || j < 0 || j >= visitedMat[0].length || visitedMat[i][j] == true)
            return 0;
        visitedMat[i][j] = true;
        if (reachable(i, j, k)) {
            int count = 1 + recursiveCount(visitedMat, i + 1, j, k) + recursiveCount(visitedMat, i, j + 1, k);
            return count;
        }
        return 0;
    }

    private boolean reachable(int i, int j, int k) {
        int sum = 0;
        while (i > 0) {
            sum += i % 10;
            i = i / 10;
        }
        while (j > 0) {
            sum += j % 10;
            j = j / 10;
        }
        if (sum <= k)
            return true;
        return false;
    }
}
```