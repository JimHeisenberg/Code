# 剑指 Offer 07. 重建二叉树

输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如，给出
```
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
```
返回如下的二叉树：
```
    3
   / \
  9  20
    /  \
   15   7
```
限制：

0 <= 节点个数 <= 5000

注意：本题与主站 105 题重复：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
先序遍历的第一个节点，是二叉树的根节点，这个节点在中序遍历中可以把左右子树分开  
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
class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return recursivelyBuildTree(preorder, 0, preorder.length, inorder, 0, inorder.length);
    }

    private TreeNode recursivelyBuildTree(int[] preorder, int preorderStart, int preorderEnd, int[] inorder,
            int inorderStart, int inOrderEnd) {
        if (preorderStart >= preorderEnd)
            return null;
        int x = preorder[preorderStart];
        int inorderEndLeft = indexOf(x, inorder, inorderStart, inOrderEnd);
        int preorderEndLeft = inorderEndLeft - inorderStart + preorderStart + 1;
        TreeNode node = new TreeNode(x);
        node.left = recursivelyBuildTree(preorder, preorderStart + 1, preorderEndLeft, inorder, inorderStart,
                inorderEndLeft);
        node.right = recursivelyBuildTree(preorder, preorderEndLeft, preorderEnd, inorder, inorderEndLeft + 1,
                inOrderEnd);
        return node;
    }

    private int indexOf(int target, int[] list, int s, int e) {
        // 用二分查找还可以加速
        for (int i = s; i < e; i++) {
            if (target == list[i])
                return i;
        }
        return -1;
    }
}
```

# Solution 2
先序遍历的第一个节点，是二叉树的根节点，这个节点在中序遍历中可以把左右子树分开  
加强了鲁棒性，处理了先序中序不匹配  
利用哈希表对查找加速  
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
class Solution {

    HashMap<Integer, Integer> indexMap;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        indexMap = new HashMap<>();
        for (int i = 0; i < inorder.length; i++)
            indexMap.put(inorder[i], i);
        return recursivelyBuildTree(preorder, 0, preorder.length, inorder, 0, inorder.length);
    }

    private TreeNode recursivelyBuildTree(int[] preorder, int preorderStart, int preorderEnd, int[] inorder,
            int inorderStart, int inOrderEnd) {
        if (preorderStart >= preorderEnd)
            return null;
        int x = preorder[preorderStart];
        int inorderEndLeft = indexOf(x, inorder, inorderStart, inOrderEnd);
        // 先序中序不匹配
        if (inorderEndLeft == -1)
            return null;
        int preorderEndLeft = inorderEndLeft - inorderStart + preorderStart + 1;
        TreeNode node = new TreeNode(x);
        node.left = recursivelyBuildTree(preorder, preorderStart + 1, preorderEndLeft, inorder, inorderStart,
                inorderEndLeft);
        node.right = recursivelyBuildTree(preorder, preorderEndLeft, preorderEnd, inorder, inorderEndLeft + 1,
                inOrderEnd);
        return node;
    }

    private int indexOf(int target, int[] list, int s, int e) {
        Integer index = indexMap.get(target);
        if (index == null || index < s || index >= e) {
            return -1;
        }
        return index;
    }
}
```