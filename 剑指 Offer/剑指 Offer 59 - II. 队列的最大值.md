# 剑指 Offer 59 - II. 队列的最大值

请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：
```
输入: 
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
```
示例 2：
```
输入: 
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
```
限制：
+ 1 <= push_back,pop_front,max_value的总操作数 <= 10000
+ 1 <= value <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
用一个非增的最大值队列记录最大值  
如果在数据队列插入一个元素x，这个元素大于队列数据队列中后n个元素。则这后n个元素出队列后，队列最大值应该为x，直到x出队列。所以，可以插入x的时候，从后往前删除最大值队列中小于x的元素  
插入操作虽然看起来有循环，做一个插入操作时最多可能会有 n 次出队操作。但要注意，由于每个数字只会出队一次，因此对于所有的 n 个数字的插入过程，对应的所有出队操作也不会大于 n 次。因此将出队的时间均摊到每个插入操作上，时间复杂度为 O(1)。  
``` java
import java.util.*;

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

/**
 * Your MaxQueue object will be instantiated and called as such:
 * MaxQueue obj = new MaxQueue();
 * int param_1 = obj.max_value();
 * obj.push_back(value);
 * int param_3 = obj.pop_front();
 */
```