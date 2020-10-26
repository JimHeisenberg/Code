# 剑指 Offer 32 - III. 从上到下打印二叉树 III

请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

例如:
给定二叉树: [3,9,20,null,null,15,7],
```
    3
   / \
  9  20
    /  \
   15   7
```
返回其层次遍历结果：
```
[
  [3],
  [20,9],
  [15,7]
]
```
提示：
+ 节点总数 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
利用队列进行遍历  
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
    public List<List<Integer>> levelOrder(TreeNode root) {
        if (root == null)
            return new ArrayList<List<Integer>>();
        Queue<TreeNode> mainQueue = new LinkedList<TreeNode>();
        Queue<TreeNode> subQueue = new LinkedList<TreeNode>();
        Queue<TreeNode> emptyQueueTemp;
        List<List<Integer>> result = new LinkedList<List<Integer>>();
        List<Integer> buffer;
        boolean evenLine = false;
        mainQueue.offer(root);
        while (!mainQueue.isEmpty()) {
            buffer = new LinkedList<>();
            while (!mainQueue.isEmpty()) {
                TreeNode node = mainQueue.poll();
                buffer.add(node.val);
                if (node.left != null)
                    subQueue.offer(node.left);
                if (node.right != null)
                    subQueue.offer(node.right);
            }
            emptyQueueTemp = mainQueue;
            mainQueue = subQueue;
            subQueue = emptyQueueTemp;
            if (evenLine) {
                evenLine = false;
                buffer = reverse(buffer);
            } else {
                evenLine = true;
            }
            result.add(buffer);
        }
        return result;
    }

    private List<Integer> reverse(List<Integer> origin) {
        List<Integer> reversed = new LinkedList<>();
        for (Integer integer : origin)
            reversed.add(0, integer);
        return reversed;
    }
}
```