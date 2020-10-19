# 剑指 Offer 19. 正则表达式匹配

请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

示例 1:
```
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
```
示例 2:
```
输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
```
示例 3:
```
输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
```
示例 4:
```
输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
```
示例 5:
```
输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
```
+ s 可能为空，且只包含从 a-z 的小写字母。
+ p 可能为空，且只包含从 a-z 的小写字母以及字符 . 和 *，无连续的 '*'。

注意：本题与主站 10 题相同：https://leetcode-cn.com/problems/regular-expression-matching/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
动态规划，java version  
``` java
class Solution {
    public boolean isMatch(String s, String p) {
        boolean[][] matrix = new boolean[s.length() + 1][p.length() + 1];
        matrix[0][0] = true;
        for (int i = 0; i <= s.length(); i++) {
            for (int j = 1; j <= p.length(); j++) {
                if (p.charAt(j - 1) == '*') {
                    matrix[i][j] |= matrix[i][j - 2];
                    if (matches(s, p, i, j - 1))
                        matrix[i][j] |= matrix[i - 1][j];
                } else {
                    if (matches(s, p, i, j))
                        matrix[i][j] |= matrix[i - 1][j - 1];
                }
            }
        }
        return matrix[s.length()][p.length()];
    }

    private boolean matches(String s, String p, int i, int j) {
        if (i == 0)
            return false;
        if (p.charAt(j - 1) == '.')
            return true;
        return s.charAt(i - 1) == p.charAt(j - 1);
    }
}
```

动态规划，C version  
``` c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool matches(char *s, char *p, int **f, int i, int j);

bool isMatch(char *s, char *p)
{
    int s_len = strlen(s) + 1;
    int p_len = strlen(p) + 1;
    int **f;
    int i, j;
    bool result;
    f = (int **)calloc(s_len * sizeof(int *), sizeof(int *));
    for (i = 0; i < s_len; i++)
        f[i] = (int *)calloc(p_len * sizeof(int), sizeof(int));

    f[0][0] = true;
    for (i = 0; i < s_len; i++)
    {
        for (j = 1; j < p_len; j++)
        {
            if (p[j - 1] == '*')
            {
                f[i][j] |= f[i][j - 2];
                if (matches(s, p, f, i, j - 1))
                    f[i][j] |= f[i - 1][j];
            }
            else
            {
                if (matches(s, p, f, i, j))
                    f[i][j] |= f[i - 1][j - 1];
            }
        }
    }

    result = f[s_len - 1][p_len - 1];
    for (i = 0; i < s_len; i++)
        free(f[i]);
    free(f);
    return result;
}

bool matches(char *s, char *p, int **f, int i, int j)
{
    if (i == 0)
        return false;
    if (p[j - 1] == '.')
        return true;
    return s[i - 1] == p[j - 1];
}
```