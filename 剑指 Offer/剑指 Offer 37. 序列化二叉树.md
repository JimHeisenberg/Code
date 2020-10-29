# 剑指 Offer 37. 序列化二叉树

请实现两个函数，分别用来序列化和反序列化二叉树。

示例: 
```
你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
```
注意：本题与主站 297 题相同：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution 1
``` java
/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode(int x) { val = x; } }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        List<Integer> data = preorderTraversal(root, new LinkedList<Integer>());
        String result = data.toString();
        return result;
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        List<String> temp = Arrays.asList(data.substring(1, data.length() - 1).split(", "));
        List<Integer> buffer = new LinkedList<Integer>();
        for (String s : temp) {
            if (s.equals("null"))
                buffer.add(null);
            else
                buffer.add(Integer.valueOf(s));
        }
        TreeNode root = preorderRestore(buffer);
        return root;
    }

    private List<Integer> preorderTraversal(TreeNode root, List<Integer> buffer) {
        if (root == null) {
            buffer.add(null);
            return buffer;
        }
        buffer.add(root.val);
        preorderTraversal(root.left, buffer);
        preorderTraversal(root.right, buffer);
        return buffer;
    }

    private TreeNode preorderRestore(List<Integer> buffer) {
        if (buffer.isEmpty())
            return null;
        Integer val = buffer.remove(0);
        if (val == null)
            return null;
        TreeNode root = new TreeNode(val);
        root.left = preorderRestore(buffer);
        root.right = preorderRestore(buffer);
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));
```