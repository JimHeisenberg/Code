# 51N皇后II

n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

![图为 8 皇后问题的一种解法](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/8-queens.png)

上图为 8 皇后问题的一种解法。

给定一个整数 n，返回 n 皇后不同的解决方案的数量。

示例:
```
输入: 4
输出: 2
解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
```
提示：
+  皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一或 N-1 步，可进可退。（引用自 百度百科 - 皇后 ）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
递归回溯  
``` java
import java.util.*;

class Solution {
    int boardLen;
    int numberOfSolution;
    List<Boolean> row;
    List<Boolean> column;
    List<Boolean> slash;
    List<Boolean> backslash;

    public void recursiveFind(int n) {
        if (n == 0) {
            numberOfSolution += 1;
            return;
        }
        int i = boardLen - n;
        for (int j = 0; j < boardLen; j++) {
            if (row.get(i) == false && column.get(j) == false && slash.get(i + j) == false
                    && backslash.get(i + boardLen - 1 - j) == false) {
                //
                row.set(i, true);
                column.set(j, true);
                slash.set(i + j, true);
                backslash.set(i + boardLen - 1 - j, true);
                //
                recursiveFind(n - 1);
                //
                row.set(i, false);
                column.set(j, false);
                slash.set(i + j, false);
                backslash.set(i + boardLen - 1 - j, false);
            }
        }
    }

    public int totalNQueens(int n) {
        boardLen = n;
        numberOfSolution = 0;
        row = new ArrayList<>();
        column = new ArrayList<>();
        slash = new ArrayList<>();
        backslash = new ArrayList<>();
        initBoard();
        recursiveFind(n);
        return numberOfSolution;
    }

    public void initBoard() {
        for (int i = 0; i < boardLen; i++) {
            row.add(false);
        }
        for (int i = 0; i < boardLen; i++) {
            column.add(false);
        }
        for (int i = 0; i < boardLen * 2 - 1; i++) {
            slash.add(false);
        }
        for (int i = 0; i < boardLen * 2 - 1; i++) {
            backslash.add(false);
        }
    }
}
```