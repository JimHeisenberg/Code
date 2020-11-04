# 剑指 Offer 57 - II. 和为s的连续正数序列

输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

示例 1：
```
输入：target = 9
输出：[[2,3,4],[4,5]]
```
示例 2：
```
输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
```
限制：
+ 1 <= target <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
假设序列第一个数字为x，序列长度为n。有```target = n*x + (n*n-n)/2```，且```n>=2, x>=1, n&x∈N+```  
令x=1，可得n的上界，再利用上界遍历反求x  
``` java
import java.util.*;
import java.lang.Math;

class Solution {
    public int[][] findContinuousSequence(int target) {
        double nUpperBound = (Math.sqrt(2 * target + 0.25) - 0.5);
        int nMax = (int) (nUpperBound + Double.MIN_NORMAL);
        List<int[]> data = new ArrayList<>();
        for (int n = nMax; n >= 2; n--) {
            int nx = target - n * (n - 1) / 2;
            int x = nx / n;
            if (n * x == nx) {
                int[] line = new int[n];
                for (int i = 0; i < line.length; i++)
                    line[i] = x++;
                data.add(line);
            }
        }
        int[][] result = new int[data.size()][];
        for (int i = 0; i < result.length; i++)
            result[i] = data.get(i);
        return result;
    }
}
```