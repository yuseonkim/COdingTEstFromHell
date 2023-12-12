package org.example.baekjoon.GOLD.가운데를말해요;

import java.io.*;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
/*
            1. 홀수번째 숫자이면 maxHeap에 짝수번째 숫자이면 minHeap에 넣어주기
            2. maxHeap의 노드가 minHeap의 노드보다 큰 경우 자리 바꿔주기
            3. 매 라운드마다 maxHeap의 노드가 결과
             */
        for (int i = 1; i <= N; i++) {
            int number = Integer.parseInt(br.readLine());
            if (isOdd(i)) {
                maxHeap.add(number);
            } else {
                minHeap.add(number);
            }
            if(!maxHeap.isEmpty() && !minHeap.isEmpty() && (maxHeap.peek() > minHeap.peek())){
                int maxHeapRoot = maxHeap.poll();
                int minHeapRoot = minHeap.poll();
                maxHeap.add(minHeapRoot);
                minHeap.add(maxHeapRoot);
            }
            bw.write(String.valueOf(maxHeap.peek()));
            bw.newLine();;
        }
        bw.flush();

    }

    public static boolean isOdd(int n) {
        return n % 2 != 0;
    }
}
