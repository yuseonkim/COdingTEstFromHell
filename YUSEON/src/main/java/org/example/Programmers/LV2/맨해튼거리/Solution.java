package org.example.Programmers.LV2.맨해튼거리;

import java.util.ArrayList;
import java.util.List;
public class Solution {
    public static List<Integer> solution(String[][] places) {
        List<Integer> result = new ArrayList<>();

        for (String[] place : places) {
            List<int[]> persons = new ArrayList<>();
            List<int[]> partitions = new ArrayList<>();

            // 사람과 칸막이 위치 찾기
            for (int i = 0; i < place.length; i++) {
                for (int j = 0; j < place[i].length(); j++) {
                    char current = place[i].charAt(j);
                    if (current == 'P') {
                        persons.add(new int[]{i, j});
                    } else if (current == 'X') {
                        partitions.add(new int[]{i, j});
                    }
                }
            }

            boolean isOk = true;
            for (int i = 0; i < persons.size() && isOk; i++) {
                for (int j = i + 1; j < persons.size() && isOk; j++) {
                    int distance = manhattanDistance(persons.get(i), persons.get(j));
                    if (distance <= 2) {
                        isOk = checkPartition(persons.get(i), persons.get(j), partitions);
                    }
                }
            }

            result.add(isOk ? 1 : 0);
        }
        return result;
    }

    private static boolean checkPartition(int[] person1, int[] person2, List<int[]> partitions) {
        int xDiff = person1[0] - person2[0];
        int yDiff = person1[1] - person2[1];

        // 붙어있을 시 불가
        if (Math.abs(xDiff) + Math.abs(yDiff) == 1) {
            return false;
        }

        // 사이에 칸막이가 있는지 확인
        if (Math.abs(xDiff) == 2 && yDiff == 0) {
            return containsPartition(partitions, new int[]{(person1[0] + person2[0]) / 2, person1[1]});
        } else if (xDiff == 0 && Math.abs(yDiff) == 2) {
            return containsPartition(partitions, new int[]{person1[0], (person1[1] + person2[1]) / 2});
        } else if (Math.abs(xDiff) == 1 && Math.abs(yDiff) == 1) {
            return containsPartition(partitions, new int[]{person1[0], person2[1]}) && containsPartition(partitions, new int[]{person2[0], person1[1]});
        }

        return true;
    }

    private static boolean containsPartition(List<int[]> partitions, int[] point) {
        for (int[] partition : partitions) {
            if (partition[0] == point[0] && partition[1] == point[1]) {
                return true;
            }
        }
        return false;
    }

    private static int manhattanDistance(int[] point1, int[] point2) {
        return Math.abs(point1[0] - point2[0]) + Math.abs(point1[1] - point2[1]);
    }


    public static void main(String[] args) {
        String[][] places = {{"POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"}, {"POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"}, {"PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"}, {"OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"}, {"PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"}};
        List<Integer> arr = solution(places);
        for(int i : arr){
            System.out.println(i);
        }
    }

}
