# 剑指 Offer 35. 复杂链表的复制

请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

示例 1：
![1](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/09/e1.png)
```
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
```
示例 2：
![2](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/09/e2.png)
```
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
```
示例 3：
![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/09/e3.png)
```
输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
```
示例 4：
```
输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
```
提示：
+ -10000 <= Node.val <= 10000
+ Node.random 为空（null）或指向链表中的节点。
+ 节点数目不超过 1000 。

注意：本题与主站 138 题相同：https://leetcode-cn.com/problems/copy-list-with-random-pointer/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
1在duplicate()中对节点进行复制，新节点插入到原本节点与原本节点的下一个节点之间。
这样做是为了之后方便对复制后节点的random指向的节点进行定位。  
2在changeRandomPtr()中，改变新节点的random指针，其应为原节点的random指向的节点的下一个节点。  
3最后拆分链表，把原链表还原并提取出新链表。  
``` java
/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/
class Solution {
    public Node copyRandomList(Node head) {
        duplicate(head);
        changeRandomPtr(head);
        return split(head);
    }

    private void duplicate(Node head) {
        while (head != null) {
            Node node = new Node(head.val);
            node.next = head.next;
            head.next = node;
            head = node.next;
        }
    }

    private void changeRandomPtr(Node head) {
        while (head != null) {
            Node node = head.next;
            if (head.random == null)
                node.random = null;
            else
                node.random = head.random.next;
            head = node.next;
        }
    }

    private Node split(Node head) {
        if (head == null)
            return null;
        Node _head_ = head.next;
        while (head != null && head.next != null) {
            Node node = head.next;
            head.next = node.next;
            head = node;
        }
        return _head_;
    }
}
```