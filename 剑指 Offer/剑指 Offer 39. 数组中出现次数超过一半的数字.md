# 剑指 Offer 39. 数组中出现次数超过一半的数字

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
```
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2
```
限制：
+ 1 <= 数组长度 <= 50000

注意：本题与主站 169 题相同：https://leetcode-cn.com/problems/majority-element/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
一次遍历，哈希表计数  
``` java
import java.util.*;

class Solution {
    public int majorityElement(int[] nums) {

        Map<Integer, Integer> dict = new HashMap<>();
        for (int k : nums) {
            if (dict.containsKey(k))
                dict.replace(k, dict.get(k) + 1);
            else
                dict.put(k, 1);
        }
        int result = 0, count = 0;
        for (Integer k : dict.keySet()) {
            int keyCount = dict.get(k);
            if (count < keyCount) {
                count = keyCount;
                result = k;
            }
        }
        return result;
    }
}
```

# Solution 2
利用数组本身的特性，即结果出现的次数比其他数字加起来都多  
用result保存已经遍历部分中出现次数最多的值  
用count保存已经遍历部分中result出现次数减去其他数字出现次数  
如果count在途中变为0，说明这一段中，数字出现次数最多的占一半，其他占一半，所以这一段可以被忽视  
``` java
class Solution {
    public int majorityElement(int[] nums) {
        int result = 0, count = 0;
        for (int num : nums) {
            if (num == result) {
                count++;
            } else {
                count--;
                if (count <= 0) {
                    result = num;
                    count = 1;
                }
            }
        }
        return result;
    }
}
```