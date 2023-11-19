package org.example.Programmers.LV2.방금그곡;

import java.util.ArrayList;
import java.util.Arrays;

public class Solution {
    static public String solution(String m, String[] musicinfos) {
        String answer = "(None)";
        String[][] arr = new String[musicinfos.length][4];
        m = m.replaceAll("C#", "c");
        m = m.replaceAll("D#", "d");
        m = m.replaceAll("F#", "f");
        m = m.replaceAll("G#", "g");
        m = m.replaceAll("A#", "a");
        m = m.replaceAll("E#", "e");
        for (int i = 0; i < musicinfos.length; i++) {
            arr[i] = musicinfos[i].split(",");
        }
        for (int i = 0; i < musicinfos.length; i++) {
            arr[i][3] = arr[i][3].replaceAll("C#", "c");
            arr[i][3] = arr[i][3].replaceAll("D#", "d");
            arr[i][3] = arr[i][3].replaceAll("F#", "f");
            arr[i][3] = arr[i][3].replaceAll("G#", "g");
            arr[i][3] = arr[i][3].replaceAll("A#", "a");
            arr[i][3] = arr[i][3].replaceAll("E#", "e");
        }

        int[] time = new int[musicinfos.length];
        for (int i = 0; i < musicinfos.length; i++) {
            int tenHour1 = arr[i][0].charAt(0);
            int oneHour1 = arr[i][0].charAt(1);
            int tenMinute1 = arr[i][0].charAt(3);
            int oneMinute1 = arr[i][0].charAt(4);
            int tenHour2 = arr[i][1].charAt(0);
            int oneHour2 = arr[i][1].charAt(1);
            int tenMinute2 = arr[i][1].charAt(3);
            int oneMinute2 = arr[i][1].charAt(4);

            int startTime = (tenHour1 * 10 + oneHour1) * 60 + tenMinute1 * 10 + oneMinute1;
            int endTime = (tenHour2 * 10 + oneHour2) * 60 + tenMinute2 * 10 + oneMinute2;

            time[i] = endTime - startTime;
            System.out.println(time[i]);
        }
        for (int i = 0; i < musicinfos.length; i++) {
            arr[i][0] = String.valueOf(time[i]);
        }

        Arrays.sort(arr, (o1, o2) -> {
            return Integer.parseInt(o2[0]) - Integer.parseInt(o1[0]);
        });
        String[] newStr = new String[musicinfos.length];

        for (String a : newStr) {
            a = null;
        }
        System.out.println(m);
        for (int i = 0; i < musicinfos.length; i++) {
            for (int j = 0; j < Integer.parseInt(arr[i][0]); j++) {
                //시간이 12 길이가 5 012340123401
                newStr[i] = newStr[i] + arr[i][3].charAt(j % arr[i][3].length());
            }
            System.out.println(newStr[i]);
        }

        ArrayList<String> array = new ArrayList<>();
        for (int i = 0; i < musicinfos.length; i++) {
            if (newStr[i].contains(m)) {
                answer = arr[i][2];
                break;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        String m = "A";
        String[] musicinfos = {"03:00,03:10,FOO,B", "04:00,04:08,BAR,C"};
        System.out.println(solution(m, musicinfos));

    }
}
