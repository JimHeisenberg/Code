# 剑指 Offer 59 - I. 滑动窗口的最大值

给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:
```
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```
提示：

你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。

注意：本题与主站 239 题相同：https://leetcode-cn.com/problems/sliding-window-maximum/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
用一个非增的最大值队列记录最大值  
如果在数据队列插入一个元素x，这个元素大于队列数据队列中后n个元素。则这后n个元素出队列后，队列最大值应该为x，直到x出队列。所以，可以插入x的时候，从后往前删除最大值队列中小于x的元素  
插入操作虽然看起来有循环，做一个插入操作时最多可能会有 n 次出队操作。但要注意，由于每个数字只会出队一次，因此对于所有的 n 个数字的插入过程，对应的所有出队操作也不会大于 n 次。因此将出队的时间均摊到每个插入操作上，时间复杂度为 O(1)。  
``` java
import java.util.*;

class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums.length < k || k == 0)
            return new int[0];
        int[] result = new int[nums.length - k + 1];
        int resultIndex = 0;
        MaxQueue maxQueue = new MaxQueue();
        for (int i = 0; i < k; i++)
            maxQueue.push_back(nums[i]);
        result[resultIndex++] = maxQueue.max_value();
        for (int i = k; i < nums.length; i++) {
            maxQueue.push_back(nums[i]);
            maxQueue.pop_front();
            result[resultIndex++] = maxQueue.max_value();
        }
        return result;
    }
}

class MaxQueue {
    private LinkedList<Integer> dataQueue;
    private LinkedList<Integer> maxQueue;

    public MaxQueue() {
        dataQueue = new LinkedList<>();
        maxQueue = new LinkedList<>();
    }

    public int max_value() {
        if (maxQueue.isEmpty())
            return -1;
        return maxQueue.peek();
    }

    public void push_back(int value) {
        dataQueue.offer(value);
        while (!maxQueue.isEmpty() && maxQueue.peekLast() < value)
            maxQueue.removeLast();
        maxQueue.offer(value);
    }

    public int pop_front() {
        if (dataQueue.isEmpty())
            return -1;
        int result = dataQueue.poll();
        if (maxQueue.peek() == result)
            maxQueue.poll();
        return result;
    }
}
```