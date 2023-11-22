package org.example.Programmers.LV2.과제진행하기;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Stack;

class Solution {
    public static List<String> solution(String[][] plans) {
        List<Integer> resultInteger = new ArrayList<>();
        //시간:분 형태 -> 분으로 변경
        for (String[] plan : plans) {
            plan[1] = timeToMinute(plan[1]);
            System.out.println(plan[1]);
        }

        //시작시간 , 진행시간 map에 저장
        HashMap<Integer, Integer> map = new HashMap<>();
        HashMap<Integer, String> map2 = new HashMap<>();
        for (String[] plan : plans) {
            map.put(Integer.parseInt(plan[1]), Integer.parseInt(plan[2]));
        }
        for (String[] plan : plans) {
            map2.put(Integer.parseInt(plan[1]), plan[0]);
        }

        Stack<Integer> execute = new Stack<>();
        // 00분부터 23:50분까지
        for (int i = 0; i < 1440; i++) {
            if (!execute.empty()) {
                map.put(execute.peek(), map.get(execute.peek()) - 1);
            }
            if (!execute.empty() && map.get(execute.peek()) == 0) {
                resultInteger.add(execute.pop());
            }
            if (map.containsKey(i)) {
                execute.push(i);
            }
        }

        List<String> result = new ArrayList<>();
        for (int i : resultInteger) {
            result.add(map2.get(i));
        }
        return result;
    }

    public static String timeToMinute(String time) {
        String[] hourMinute = time.split(":");
        return String.valueOf(Integer.parseInt(hourMinute[0]) * 60 + Integer.parseInt(hourMinute[1]));
    }

    public static void main(String[] args) {
        String[][] plans = {{"korean", "00:00", "3"}, {"english", "00:01", "3"}, {"math", "00:02", "3"}};
        List<String> result = solution(plans);
        System.out.println("result : ");
        for (String i : result) {
            System.out.println(i);
        }
    }
}
