

实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:
```
输入: haystack = "hello", needle = "ll"
输出: 2
```
示例 2:
```
输入: haystack = "aaaaa", needle = "bba"
输出: -1
```
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-strstr
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
KMP  
执行用时：0 ms  
内存消耗：5.9 MB  
``` c
int *get_next(char *str)
{
    int len = strlen(str);
    int *next = malloc(len * sizeof(int));
    int i = 0, j = 0;
    next[0] = -1;
    for (i = 1; i < len; i++, j++)
    {
        next[i] = j;
        while (j >= 0 && str[i] != str[j])
            j = next[j];
    }
    return next;
}

int strStr(char *haystack, char *needle)
{
    if (*needle == '\0')
        return 0;
    int haystack_size = strlen(haystack);
    int needle_size = strlen(needle);
    int i = 0, j = 0;
    int *next = get_next(needle);
    while (i < haystack_size && j < needle_size)
    {
        if (j == -1 || haystack[i] == needle[j])
        {
            i++;
            j++;
        }
        else
        {
            j = next[j];
        }
    }
    free(next);
    if (j == needle_size)
        return i - j;
    else
        return -1;
}
```