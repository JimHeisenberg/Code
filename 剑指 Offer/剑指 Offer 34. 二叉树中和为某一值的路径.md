# 剑指 Offer 34. 二叉树中和为某一值的路径

输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

示例:
给定如下二叉树，以及目标和 sum = 22，
```
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
```
返回:
```
[
   [5,4,11,2],
   [5,8,4,5]
]
```
提示：
+ 节点总数 <= 10000

注意：本题与主站 113 题相同：https://leetcode-cn.com/problems/path-sum-ii/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
``` java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
import java.util.*;

class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> result = new LinkedList<List<Integer>>();
        Stack<Integer> stack = new Stack<>();
        recursiveFindPath(result, stack, root, sum);
        return result;
    }

    private void recursiveFindPath(List<List<Integer>> result, Stack<Integer> stack, TreeNode root, int target) {
        if (root == null)
            return;
        if (root.val == target && root.left == null && root.right == null) {
            List<Integer> temp = new LinkedList<>();
            for (Integer integer : stack)
                temp.add(integer);
            temp.add(root.val);
            result.add(temp);
        } else {
            target -= root.val;
            stack.push(root.val);
            recursiveFindPath(result, stack, root.left, target);
            recursiveFindPath(result, stack, root.right, target);
            stack.pop();
        }
    }
}
```