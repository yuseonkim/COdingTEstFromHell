package org.example.Programmers.LV1.키패드누르기;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Objects;

public class Solution {
    public static String solution(int[] numbers, String hand) {
        HashMap<Integer, int[]> hashMap = new HashMap<>();
        hashMap.put(1, new int[]{1, 4});
        hashMap.put(2, new int[]{2, 4});
        hashMap.put(3, new int[]{3, 4});
        hashMap.put(4, new int[]{1, 3});
        hashMap.put(5, new int[]{2, 3});
        hashMap.put(6, new int[]{3, 3});
        hashMap.put(7, new int[]{1, 2});
        hashMap.put(8, new int[]{2, 2});
        hashMap.put(9, new int[]{3, 2});
        hashMap.put(0, new int[]{2, 1});

        int[] left = new int[]{1,1};
        int[] right = new int[]{3,1};
        Boolean isRight = Objects.equals(hand, "right");
        StringBuilder result = new StringBuilder();

        for(int i : numbers){
            System.out.println();
            for(int a : left){
                System.out.print(a+" left");
            }
            System.out.println();
            for(int a : right){
                System.out.print(a+" right");
            }
            if(i == 1 || i == 4|| i == 7){
                left = hashMap.get(i);
                result.append("L");
            }
            if(i == 3 || i == 6 || i == 9){
                right = hashMap.get(i);
                result.append("R");
            }
            if(i == 2 || i == 5 || i == 8 || i == 0) {
                if(getDistance(left,hashMap.get(i))>getDistance(right,hashMap.get(i))){
                    right = hashMap.get(i);
                    result.append("R");
                }else if(getDistance(left,hashMap.get(i))<getDistance(right,hashMap.get(i))){
                    left = hashMap.get(i);
                    result.append("L");

                }else{
                    if(isRight){
                        right = hashMap.get(i);
                        result.append("R");
                    }else{
                        left = hashMap.get(i);
                        result.append("L");
                    }

                }
            }
        }
            return String.valueOf(result);
    }

    public static int getDistance(int[] a, int[] b){
        return Math.abs(a[0]-b[0])+Math.abs(a[1]-b[1]);
    }

    public static void main(String[] args) {
        int[] numbers = {1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5};
        System.out.println(solution(numbers, "right"));
    }
}
