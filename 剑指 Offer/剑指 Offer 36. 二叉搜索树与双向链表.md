# 剑指 Offer 36. 二叉搜索树与双向链表

输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

为了让您更好地理解问题，以下面的二叉搜索树为例：
![1](https://assets.leetcode.com/uploads/2018/10/12/bstdlloriginalbst.png)

我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。
![2](https://assets.leetcode.com/uploads/2018/10/12/bstdllreturndll.png)

特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。

注意：本题与主站 426 题相同：https://leetcode-cn.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

注意：此题对比原题有改动。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
递归处理，在中序遍历的基础上修改  
``` java
/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val,Node _left,Node _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/
class Solution {
    public Node treeToDoublyList(Node root) {
        if (root == null)
            return null;
        Node head = root;
        while (head.left != null)
            head = head.left;
        recursiveRebuild(root);
        Node tail = head;
        while (tail.right != null)
            tail = tail.right;
        head.left = tail;
        tail.right = head;
        return head;
    }

    private void recursiveRebuild(Node root) {
        if (root == null)
            return;
        Node before = root.left;
        Node after = root.right;
        if (before != null)
            while (before.right != null)
                before = before.right;
        if (after != null)
            while (after.left != null)
                after = after.left;
        recursiveRebuild(root.left);
        root.left = before;
        if (before != null)
            before.right = root;
        recursiveRebuild(root.right);
        root.right = after;
        if (after != null)
            after.left = root;
    }
}
```

# Solution 2
递归处理，在中序遍历的基础上修改  
在solution 1的基础上，用全局变量记录结果，稍微优化。  
``` java
/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val,Node _left,Node _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/
class Solution {
    Node head, before;

    public Node treeToDoublyList(Node root) {
        if (root == null)
            return null;
        head = before = null;
        recursiveRebuild(root);
        head.left = before;
        before.right = head;
        return head;
    }

    private void recursiveRebuild(Node node) {
        if (node == null)
            return;
        recursiveRebuild(node.left);
        node.left = before;
        if (before != null)
            before.right = node;
        else
            head = node;
        before = node;
        recursiveRebuild(node.right);
    }
}
```