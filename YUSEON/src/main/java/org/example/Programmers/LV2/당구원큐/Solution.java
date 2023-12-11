package org.example.Programmers.LV2.당구원큐;

import java.util.ArrayList;
import java.util.List;

class Solution {
    public static List<Integer> solution(int m, int n, int startX, int startY, int[][] balls) {
        List<Integer> result = new ArrayList<>();
        for(int[] ball : balls){
            result.add(Math.min(distance1(m,startX,startY,ball),distance2(n,startX,startY,ball)));
        }
        return result;
    }

    public static int distance1(int m, int startX,int startY,int[] ball){
        // (2 7) (3 7) -> 0
        int endX = ball[0];
        int endY = ball[1];
        int distanceY = Math.abs(startY - endY);
        int distanceX = Math.min(m-startX + m-endX,startX+endX);
        if(distanceY == 0){
            if(startX < endX){
                distanceX = startX+endX;
            }
            if(startX > endX){
                distanceX = m- startX + m-endX;
            }
        }
        return distanceX*distanceX + distanceY*distanceY;
    }
    public static int distance2(int n,int startX,int startY,int[] ball){
        int endX = ball[0];
        int endY = ball[1];
        int distanceX = Math.abs(startX - endX);
        int distanceY = Math.min(n-startY + n-endY,startY+endY);
        if(distanceX == 0){
            if(startY < endY){
                distanceY = startY+endY;
            }
            if(startY > endY){
                distanceY = n- startY + n-endY;
            }
        }
        return distanceX*distanceX + distanceY*distanceY;
    }

    public static void main(String[] args) {
        int[][] balls = {{7, 7}, {2, 7}, {7, 3}};
        int m = 10;
        int n = 10;
        int startX = 3;
        int startY = 7;
        for(int i : solution(m,n,startX,startY,balls)){
            System.out.println(i);
        }
    }
}
