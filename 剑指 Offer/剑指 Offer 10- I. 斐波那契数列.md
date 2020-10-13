# 剑指 Offer 10- I. 斐波那契数列

写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：
```
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
```
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：
```
输入：n = 2
输出：1
```
示例 2：
```
输入：n = 5
输出：5
```
提示：
+ 0 <= n <= 100

注意：本题与主站 509 题相同：https://leetcode-cn.com/problems/fibonacci-number/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
递归效率过低，不考虑  
a=f(n), b=f(n+1), c=f(n+2)  
时间复杂度O(n), 空间复杂度O(1)  
``` java
class Solution {
    public int fib(int n) {
        // a=f(n), b=f(n+1), c=f(n+2)
        int a = 0;
        int b = 1;
        int c = 1;
        for (int i = 0; i < n; i++) {
            a = b;
            b = c;
            c = a + b;
            if (c > 1e9 + 7)
                c -= 1e9 + 7;
        }
        return a;
    }
}
```

# Solution 2
矩阵快速幂  
``` java
class Solution {

    public int fib(int n) {
        // 矩阵快速幂
        if (n <= 1)
            return n;
        long result = fastPow(n - 1).upperLeft;
        return (int) result;
    }

    FibMatrix fastPow(int n) {
        if (n == 1)
            return new FibMatrix();
        else if (n % 2 == 1) {
            FibMatrix temp = fastPow(n / 2);
            return temp.dot(temp).dot(new FibMatrix());
        } else {
            FibMatrix temp = fastPow(n / 2);
            return temp.dot(temp);
        }
    }

}

class FibMatrix {

    long upperLeft;
    long upperRight;
    long downLeft;
    long downRight;

    FibMatrix() {
        this.upperLeft = 1;
        this.upperRight = 1;
        this.downLeft = 1;
        this.downRight = 0;
    }

    FibMatrix(long upperLeft, long upperRight, long downLeft, long downRight) {
        this.upperLeft = upperLeft % (1000000007);
        this.upperRight = upperRight % (1000000007);
        this.downLeft = downLeft % (1000000007);
        this.downRight = downRight % (1000000007);
    }

    FibMatrix dot(FibMatrix mat) {
        long newUpperLeft = this.upperLeft * mat.upperLeft + this.upperRight * mat.downLeft;
        long newUpperRight = this.upperLeft * mat.upperRight + this.upperRight * mat.downRight;
        long newDownLeft = this.downLeft * mat.upperLeft + this.downRight * mat.downLeft;
        long newDownRight = this.downLeft * mat.upperRight + this.downRight * mat.downRight;
        return new FibMatrix(newUpperLeft, newUpperRight, newDownLeft, newDownRight);
    }
}
```

# Solution 3
通项公式  
double存在精度丢失，过不了测试用例  
``` java
class Solution {
    public int fib(int n) {
        // a = (1+√5)/2
        // b = (1-√5)/2
        // c = √5
        // f(n) = (aⁿ - bⁿ) / c
        double a = (1 + Math.sqrt(5)) / 2;
        double b = (1 - Math.sqrt(5)) / 2;
        double c = Math.sqrt(5);
        double result = (Math.pow(a, n) - Math.pow(b, n)) / c;
        result %= 1e9 + 7;
        return (int) result;
    }
}
```