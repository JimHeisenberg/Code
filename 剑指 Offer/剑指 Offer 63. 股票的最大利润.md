# 剑指 Offer 63. 股票的最大利润

假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

示例 1:
```
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
```
示例 2:
```
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
```
限制：
+ 0 <= 数组长度 <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
必须先买再卖，如果两两枚举要 O(n²)的时间  
但是如果固定卖出价格，求之前最低买入价格，从而算差价，只要 O(n)的时间  
``` java
class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length <= 1)
            return 0;
        int minPriceBefore = prices[0];
        int result = 0;
        for (int i = 1; i < prices.length; i++) {
            result = Integer.max(result, prices[i] - minPriceBefore);
            minPriceBefore = Integer.min(minPriceBefore, prices[i]);
        }
        return result;
    }
}
```