    public String largestNumber(int[] nums) {
    if (nums == null || nums.length == 0) {
        return "";
    }
    // 将每个数字转换成字符串
    String[] strs = new String[nums.length];
    for (int i = 0; i < nums.length; i++) {
        strs[i] = String.valueOf(nums[i]);
    }
    // 自定义比较规则
    Arrays.sort(strs, new Comparator<String>() {
        public int compare(String s1, String s2) {
            String order1 = s1 + s2;
            String order2 = s2 + s1;
            return order2.compareTo(order1);
        }
    });
    // 特殊情况处理
    if (strs[0].equals("0")) {
        return "0";
    }
    // 将排序后的字符串连接起来
    StringBuilder sb = new StringBuilder();
    for (String str : strs) {
        sb.append(str);
    }
    return sb.toString();
    }