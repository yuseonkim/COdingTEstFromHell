//package org.example.baekjoon.GOLD.평범한배낭;
//
//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;
//import java.util.Arrays;
//import java.util.StringTokenizer;
//import java.util.stream.Collectors;
//
//public class Main {
//    static int N , maxWeight;
//    static int maxValue = 0;
//    public static void func(int i, int weight,int value,int[][] bags){
//        if(weight > maxWeight){
//            return;
//        }
//        if(maxValue < value){
//            maxValue = value;
//        }
//        for(int j=i+1;j<N;j++){
//            func(j,weight+bags[j][0],value+bags[j][1],bags);
//        }
//
//    }
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st = new StringTokenizer(br.readLine());
//        N = Integer.parseInt(st.nextToken());
//        maxWeight = Integer.parseInt(st.nextToken());
//        int[][] bags = new int[N][2];
//        int[][] filteredBags = Arrays.stream(bags).filter(i -> i[0] <= maxWeight).collect(Collectors.toList()).toArray(new int[0][]);
//        for(int i = 0;i<N;i++){
//            StringTokenizer st2 = new StringTokenizer(br.readLine());
//            int weight = Integer.parseInt(st2.nextToken());
//            int value = Integer.parseInt(st2.nextToken());
//            bags[i][0] = weight;
//            bags[i][1] = value;
//        }
//
//        for(int i=0;i<N;i++){
//            int weight = bags[i][0];
//            int value = bags[i][1];
//            if(weight > maxWeight){
//                return;
//            }
//            if(maxValue < value){
//                maxValue = value;
//            }
//            func(i,weight,value,filteredBags);
//        }
//        System.out.println(maxValue);
//    }
//}
package org.example.baekjoon.GOLD.평범한배낭;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Main {
    static int N, maxWeight;
    static int[][] bags;
    static int[][] dp;

    public static int func(int i, int weight) {
        if (i == N) {
            return 0;
        }

        if (dp[i][weight] != -1) {
            return dp[i][weight];
        }

        if (bags[i][0] > weight) {
            return dp[i][weight] = func(i + 1, weight);
        }

        int skip = func(i + 1, weight);
        int take = bags[i][1] + func(i + 1, weight - bags[i][0]);

        return dp[i][weight] = Math.max(skip, take);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        maxWeight = Integer.parseInt(st.nextToken());

        bags = new int[N][2];
        dp = new int[N][maxWeight + 1];

        for (int[] row : dp) {
            Arrays.fill(row, -1);
        }

        for (int i = 0; i < N; i++) {
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            bags[i][0] = Integer.parseInt(st2.nextToken());
            bags[i][1] = Integer.parseInt(st2.nextToken());
        }

        int result = func(0, maxWeight);
        System.out.println(result);
    }
}
