//package org.example.Programmers.LV1.공원산책;
//
//import java.util.ArrayList;
//
//public class Solution {
//    public int[] solution(String[] park, String[] routes) {
//
//        int[] start = {0, 0};
//        ArrayList<Integer> noX = new ArrayList<>();
//        ArrayList<Integer> noY = new ArrayList<>();
//        //시작 위치 찾기
//        //장애물 위치 찾기 - 장애물이 (X,Y)이면 X에서
//        for (int i = 0; i < park.length; i++) {
//            for (int j = 0; j < park[i].length(); j++) {
//                if (park[i].charAt(j) == 'S') {
//                    start[0] = i;
//                    start[1] = j;
//                }
//                if (park[i].charAt(j) == 'S') {
//                    noX.add(i);
//                    noY.add(j);
//                }
//            }
//        }
//
//        int width = park[0].length(); //공원 가로 길이
//        int height = park.length; //공원 세로 길이
//
//        for(String route : routes){
//            int[] xy = {0,0};
//            char direction = route.charAt(0);
//            int distance = route.charAt(2) - '0';
//            if(direction == 'E'){
//                int[] arrive = {start[0]+xy[0],start[1]+xy[1]};
//                for(int x : noX){
//                    if(arrive[1] - x >= 0)
//
//                }
//
//                }
//            if(direction == 'W'){
//                xy[0] -= distance;
//            }
//            if(direction == 'N'){
//                xy[1] += distance;
//            }
//            if(direction == 'S'){
//                xy[0] -= distance;
//            }
//
//            int[] arrive = {start[0]+xy[0],start[1]+xy[1]};
//
//            if(arrive[])
//
//        }
//
//
//
//
//    }
//}
