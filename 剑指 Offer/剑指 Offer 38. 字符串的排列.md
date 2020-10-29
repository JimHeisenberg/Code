# 剑指 Offer 38. 字符串的排列

输入一个字符串，打印出该字符串中字符的所有排列。

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

示例:
```
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
```
限制：
+ 1 <= s 的长度 <= 8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
``` java
import java.util.*;

class Solution {
    public String[] permutation(String s) {
        Map<Character, Integer> dict = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char k = s.charAt(i);
            if (dict.keySet().contains(k))
                dict.replace(k, dict.get(k) + 1);
            else
                dict.put(k, 1);
        }
        StringBuilder buffer = new StringBuilder();
        List<String> data = new ArrayList<>();
        dfs(dict, buffer, data, s.length());
        String[] result = new String[data.size()];
        for (int i = 0; i < data.size(); i++)
            result[i] = data.get(i);
        return result;
    }

    private void dfs(Map<Character, Integer> dict, StringBuilder buffer, List<String> data, int length) {
        if (buffer.length() == length) {
            data.add(buffer.toString());
            return;
        }
        for (Character k : dict.keySet()) {
            Integer v = dict.get(k);
            if (v <= 0)
                continue;
            dict.replace(k, v - 1);
            buffer.append(k);
            dfs(dict, buffer, data, length);
            buffer.deleteCharAt(buffer.length() - 1);
            dict.replace(k, v);
        }
    }
}
```