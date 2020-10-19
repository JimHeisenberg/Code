# 剑指 Offer 20. 表示数值的字符串

请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
有限状态机，java version  
``` java
class Solution {
    public boolean isNumber(String s) {
        int state = 0;
        // state details (when at if clause):
        // 0 initial state or all characters before are ' '
        // 1 the character before is '+' or '-' and before '.' 'e'
        // 2 the character before in 0~9 and before '.' 'e'
        // 3 the character before is '.' and there is number before '.'
        // 4 the character before is '.' and there is no number before '.'
        // 5 the character before in 0~9 and after '.' before 'e'
        // 6 the character before is 'e'
        // 7 the character before is '+' or '-' and after '.' 'e'
        // 8 the character before in 0~9 and after '.' 'e'
        // 9 the character before is ' ' and there is already a qualified number
        // -1 return false immediately
        int[][] matrix = { { 0, -1, 9, -1, 9, 9, -1, -1, 9, 9, }, { 1, -1, -1, -1, -1, -1, 7, -1, -1, -1, },
                { 2, 2, 2, 5, 5, 5, 8, 8, 8, -1, }, { 3, 3, 4, -1, -1, -1, -1, -1, -1, -1, },
                { -1, -1, 6, -1, 6, 6, -1, -1, -1, -1, }, { -1, -1, 2, -1, 4, 5, -1, -1, 8, 9, }, };
        int rowIndex = 0;
        for (int i = 0; i < s.length(); i++) {
            switch (s.charAt(i)) {
                case ' ':
                    rowIndex = 0;
                    break;
                case '+':
                case '-':
                    rowIndex = 1;
                    break;
                case '0':
                case '1':
                case '2':
                case '3':
                case '4':
                case '5':
                case '6':
                case '7':
                case '8':
                case '9':
                    rowIndex = 2;
                    break;
                case '.':
                    rowIndex = 3;
                    break;
                case 'e':
                case 'E':
                    rowIndex = 4;
                    break;
                default:
                    return false;
            }
            state = matrix[rowIndex][state];
            if (state == -1)
                return false;
        }
        rowIndex = 5;
        state = matrix[rowIndex][state];
        if (state == -1)
            return false;
        return true;
    }
}
```

有限状态机，python version  
``` python
class Solution:
    def isNumber(self, s: str) -> bool:
        state = 0
        """
        state details (when at if clause):
            0 initial state or all characters before are ' '
            1 the character before is '+' or '-' and before '.' 'e'
            2 the character before in 0~9 and before '.' 'e'
            3 the character before is '.' and there is number before '.'
            4 the character before is '.' and there is no number before '.'
            5 the character before in 0~9 and after '.' before 'e'
            6 the character before is 'e'
            7 the character before is '+' or '-' and after '.' 'e'
            8 the character before in 0~9 and after '.' 'e'
            9 the character before is ' ' and there is already a qualified number
        """
        for c in s:
            if (c == ' '):
                if state in [1, 3, 6, 7]:
                    return False
                elif state in [0, 9]:
                    pass
                elif state in [2, 4, 5, 8]:
                    state = 9
                else:
                    raise Exception("c=' '")
            elif (c in ['+', '-']):
                if state in [1, 2, 3, 4, 5, 7, 8, 9]:
                    return False
                elif state == 0:
                    state = 1
                elif state == 6:
                    state = 7
                else:
                    raise Exception("c='+'/'-'")
            elif (c in list(map(str, range(10)))):
                if state == 9:
                    return False
                elif state in [2, 5, 8]:
                    pass
                elif state in [0, 1]:
                    state = 2
                elif state in [3, 4]:
                    state = 5
                elif state in [6, 7]:
                    state = 8
                else:
                    raise Exception("c=0~9")
            elif (c == '.'):
                if state in [3, 4, 5, 6, 7, 8, 9]:
                    return False
                elif state in [0, 1]:
                    state = 3
                elif state == 2:
                    state = 4
                else:
                    raise Exception("c='.'")
            elif (c == 'e' or c == 'E'):
                if state in [0, 1, 3, 6, 7, 8, 9]:
                    return False
                elif state in [2, 4, 5]:
                    state = 6
                else:
                    raise Exception("c=0~9")
            else:
                # raise Exception(f"unknown char {c}")
                return False
        if (state in [2, 4, 5, 8, 9]):
            return True
        else:
            return False
```