# 剑指 Offer 49. 丑数

我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

示例:
```
输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
```
说明:  
+ 1 是丑数。
+ n 不超过1690。

注意：本题与主站 264 题相同：https://leetcode-cn.com/problems/ugly-number-ii/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/chou-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
空间换取时间，记录小于n的每一个丑数  
新一个丑数字一定是前面某个丑数x2,x3,x5的结果  
see also [link](https://leetcode-cn.com/problems/chou-shu-lcof/solution/mian-shi-ti-49-chou-shu-dong-tai-gui-hua-qing-xi-t/)  
``` java
import java.util.*;

class Solution {
    public int nthUglyNumber(int n) {
        List<Integer> uglyNumbers = new ArrayList<>(n);
        uglyNumbers.add(1);
        int x2Index = 0;
        int x3Index = 0;
        int x5Index = 0;
        int x2 = 2;
        int x3 = 3;
        int x5 = 5;
        for (int i = 1; i < n; i++) {
            int uglyNumber = Integer.min(x2, Integer.min(x3, x5));
            uglyNumbers.add(uglyNumber);
            if (uglyNumber == x2)
                x2 = uglyNumbers.get(++x2Index) * 2;
            if (uglyNumber == x3)
                x3 = uglyNumbers.get(++x3Index) * 3;
            if (uglyNumber == x5)
                x5 = uglyNumbers.get(++x5Index) * 5;
        }
        return uglyNumbers.get(n - 1);
    }
}
```

# Solution 2
空间换取时间，记录小于n的每一个丑数  
在 Solution 1 的基础上，用```int[]```代替```List<Integer>```加速  
``` java
class Solution {
    public int nthUglyNumber(int n) {
        int[] uglyNumbers = new int[n];
        uglyNumbers[0] = 1;
        int x2Index = 0;
        int x3Index = 0;
        int x5Index = 0;
        int x2 = 2;
        int x3 = 3;
        int x5 = 5;
        for (int i = 1; i < n; i++) {
            int uglyNumber = Integer.min(x2, Integer.min(x3, x5));
            uglyNumbers[i] = uglyNumber;
            if (uglyNumber == x2)
                x2 = uglyNumbers[++x2Index] * 2;
            if (uglyNumber == x3)
                x3 = uglyNumbers[++x3Index] * 3;
            if (uglyNumber == x5)
                x5 = uglyNumbers[++x5Index] * 5;
        }
        return uglyNumbers[n - 1];
    }
}
```