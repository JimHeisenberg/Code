# 剑指 Offer 41. 数据流中的中位数

如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：
+ void addNum(int num) - 从数据流中添加一个整数到数据结构中。
+ double findMedian() - 返回目前所有元素的中位数。

示例 1：
```
输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]
```
示例 2：
```
输入：
["MedianFinder","addNum","findMedian","addNum","findMedian"]
[[],[2],[],[3],[]]
输出：[null,null,2.00000,null,2.50000]
```
限制：
+ 最多会对 addNum、findMedian 进行 50000 次调用。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
小顶堆+大顶堆  
``` java
class MedianFinder {
    PriorityQueue<Integer> smallPart;
    PriorityQueue<Integer> bigPart;

    /** initialize your data structure here. */
    public MedianFinder() {
        // PriorityQueue is MinHeap by default
        smallPart = new PriorityQueue<>((x, y) -> (y - x));
        bigPart = new PriorityQueue<>();
    }

    public void addNum(int num) {
        // smallPart.size() always >= bigPart.size()
        if (smallPart.size() == 0) {
            smallPart.offer(num);
        } else if (smallPart.size() == bigPart.size()) {
            if (num <= bigPart.peek()) {
                smallPart.offer(num);
            } else {
                bigPart.offer(num);
                smallPart.offer(bigPart.poll());
            }
        } else {// if (smallPart.size() > bigPart.size()) {
            if (num >= smallPart.peek()) {
                bigPart.offer(num);
            } else {
                smallPart.offer(num);
                bigPart.offer(smallPart.poll());
            }
        }
    }

    public double findMedian() {
        double result;
        if (smallPart.size() == 0)
            // IndexOutOfBoundsException
            return Double.NaN;

        if (smallPart.size() == bigPart.size())
            result = (smallPart.peek() + bigPart.peek()) / 2.0;
        else
            result = smallPart.peek();
        return result;
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */
```