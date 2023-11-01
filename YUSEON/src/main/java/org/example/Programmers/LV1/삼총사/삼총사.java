package org.example.Programmers.LV1.삼총사;

public class 삼총사 {
    static int count = 0;

    static void combination(int[] arr, boolean[] check, int start, int depth, int r) {
        if (depth == r) {
            int sum = 0;
            for (int i = 0; i < arr.length; i++) {
                if (check[i])
                    sum += arr[i];
            }
            if (sum == 0)
                count++;
            return;
        }
        for (int i = start; i < arr.length; i++) {
            if (!check[i]) {
                check[i] = true;
                combination(arr, check, i + 1, depth + 1, r);
                check[i] = false;
            }
        }
    }

    public static int solution(int[] number) {
        combination(number, new boolean[number.length], 0, 0, 3);
        return count;
    }

    public static void main(String[] args) {
        int[] arr = {-2,3,0,2,-5};
        System.out.println(solution(arr));



    }
}
