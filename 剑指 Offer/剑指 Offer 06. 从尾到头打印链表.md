# 剑指 Offer 06. 从尾到头打印链表

输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：
```
输入：head = [1,3,2]
输出：[2,3,1]
```

限制：

0 <= 链表长度 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
堆栈  
``` java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public int[] reversePrint(ListNode head) {
        ArrayList<Integer> stack = new ArrayList<>();
        while (head != null) {
            stack.add(head.val);
            head = head.next;
        }
        int[] result = new int[stack.size()];
        for (int i = 0; i < result.length; i++) {
            result[i] = stack.remove(stack.size() - 1);
        }
        return result;
    }
}
```
# Solution 2
递归  
``` java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public int[] reversePrint(ListNode head) {
        ArrayList<Integer> queue = new ArrayList<>();
        recursion(head, queue);
        int[] result = new int[queue.size()];
        for (int i = 0; i < result.length; i++) {
            result[i] = queue.get(i);
        }
        return result;
    }

    private void recursion(ListNode head, ArrayList<Integer> queue) {
        if (head == null)
            return;
        recursion(head.next, queue);
        queue.add(head.val);
    }
}
```