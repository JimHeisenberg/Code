# 剑指 Offer 60. n个骰子的点数

把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。

你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

示例 1:
```
输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
```
示例 2:
```
输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]
```
限制：
+ 1 <= n <= 11

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
递归递推  
``` java
class Solution {
    public double[] dicesProbability(int n) {
        if (n <= 0)
            return new double[0];
        double[] dice = new double[6];
        for (int i = 0; i < dice.length; i++)
            dice[i] = 1.0 / 6.0;
        if (n == 1)
            return dice;
        double[] dices = dicesProbability(n - 1);
        double[] result = new double[5 * n + 1];
        for (int i = 0; i < result.length; i++) {
            for (int j = Integer.max(0, i - 5); j < Integer.min(dices.length, i + 1); j++)
                result[i] += dices[j] / 6;
        }
        return result;
    }
}
```