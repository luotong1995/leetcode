### 求子数组个数

求满足条件的子数组，越短越合法

一般要写 ans += right - left + 1。

滑动窗口的内层循环结束时，右端点固定在right，左端点在 left,left+1,⋯ ,right的所有子数组（子串）都是合法的，这一共有 right−left+1个。